class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        n = len(s)
        m = len(t)
        if(n!=m):
            return False
        else:
            diff = {}
            d = {}
            for i in range(n):
                if(s[i]!=t[i]):
                    if(t[i]>s[i]):
                        value = ord(t[i])-ord(s[i])
                    else:
                        value = (26-ord(s[i]))+ord(t[i])
                    if value not in diff:
                        start = value
                    else:
                        start = diff[value]+26 
                    flag = 0
                    while(start<=k):
                        if start not in d:
                            d[start] = 1
                            diff[value] = start
                            flag = 1
                            break
                        start+=26
                    if(flag==0):
                        return False 
            return True
