class Solution:
    def lastSubstring(self, s: str) -> str:
        maxChar = max(s)
        
        indx = []
        
        for i in range(0, len(s)):
            if s[i] == maxChar and (i ==0 or s[i-1]!=maxChar):
                indx.append(i)
                
        
        maxind = indx[0]
        
        for i in range (1, len(indx)):
            step = 0
            curind = indx[i]
            while curind+step<len(s):
                
                if s[curind+step]>s[maxind+step]:
                    maxind = curind
                elif s[curind+step] == s[maxind+step]:
                    step+=1
                else:
                    break
                    
        return s[maxind:]

