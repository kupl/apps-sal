class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        b = 0
        flag = 0
        lis = []
        if(len(s) == len(t)):
            for i in range(len(s)):
                if(s[i] != t[i]):
                    if(s[i] < t[i]):
                        lis.append(ord(t[i]) - ord(s[i]))
                    else:
                        lis.append(26 - (ord(s[i]) - ord(t[i])))
            lis.sort()
            i = 0
            c = 0
            while(i < len(lis) - 1):
                if(lis[i] == lis[i + 1]):
                    c = c + 1
                else:
                    if(lis[i] + (c * 26) > k):
                        flag = 1
                        break
                    else:
                        c = 0
                i = i + 1
            if(len(lis) > 1):
                if(lis[-1] != lis[-2]):
                    if(lis[-1] > k):
                        flag = 1
            if(len(lis) > 0):
                if(lis[i - 1] + (c * 26) > k):
                    flag = 1
            if(flag == 0):
                b = 1
        return(b)
