class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        best = -1
        ans = []
        for i in range(2**(len(s)-1)):
            x = bin(i)
            x = x[2:]
            x = (len(s) - len(x) - 1) * '0' + x
            tmp = ''
            a = []
            c = 0
            for char in s:
                tmp += char
                if c<len(x):
                    if x[c]=='1':
                        a.append(tmp)
                        tmp = '' 
                        
                c+=1
                        
            a.append(tmp)
            
            if len(a)==len(set(a)):
                if len(a)>best:
                    best = len(a)
                    ans = a
                    
        return len(ans)

