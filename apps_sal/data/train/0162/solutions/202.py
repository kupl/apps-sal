class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[0]*(len(text2)+1) for i in range(len(text1)+1)]
        s1=text1
        s2=text2
        def helper(i1,i2):
            if memo[i1][i2]:
                return memo[i1][i2]
            if i1 == len(s1) or i2 == len(s2):
                return 0
            if s1[i1] == s2[i2]:
                memo[i1][i2] = 1+helper(i1+1,i2+1)
                
            else:
                memo[i1][i2] =  max(helper(i1+1,i2),helper(i1,i2+1))
            return memo[i1][i2]
            
        
        
        
        
        
        
        return helper(0,0)
