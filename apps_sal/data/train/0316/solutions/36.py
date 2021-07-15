class Solution:
    def longestPrefix(self, s: str) -> str:
        
        n = len(s)
        
        lps = [0]*n
        
        for i in range(1, n):
            
            j = lps[i-1]
            
            while j>0 and s[j]!=s[i]:
                j = lps[j-1]
            
            if s[j]==s[i]:
                lps[i] = j+1
        
        
        return s[:lps[n-1]]
            
        
            

