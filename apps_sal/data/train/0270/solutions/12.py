class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        def rec(x,n,s):
            
            if len(x) == n:
                r.append(x)
            else:
                for i in range(len(s)):
                    if s[i] == 'a':
                        rec(x+s[i],n,'bc')
                    elif s[i] == 'b':
                        rec(x+s[i],n,'ac')
                    else:
                        rec(x+s[i],n,'ab')
    
                    
        r = []
        rec('',n,'abc')
        
        if k<=len(r):
            return r[k-1]
        else:
            return ''
