from functools import lru_cache as memoize

class Solution():
    def longestCommonSubsequence(self, s1, s2):
        @memoize(None)
        def lcs(m,n):
            
            if(m==0 or n==0):
                return 0
            
            if s1[m-1] == s2[n-1]:
                return 1 + lcs(m-1,n-1)
            
            else:
                
                return max(lcs(m-1,n),lcs(m,n-1))
            
            
        return lcs(len(s1),len(s2))
