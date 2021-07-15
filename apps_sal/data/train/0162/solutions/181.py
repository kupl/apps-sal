class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = [[0]*len(text2) for _ in range(len(text1))]
        return self.helper(text1, 0, text2, 0, cache)
    
    def helper(self, text1:str, i:int, text2:str, j:int, cache):
        
        if i==len(text1) or j==len(text2): return 0
    
        if cache[i][j]!= 0: return cache[i][j]
        
        if text1[i]==text2[j]:
            cache[i][j] = 1+ self.helper(text1, i+1, text2, j+1, cache)
        else:
            cache[i][j] = max(self.helper(text1, i+1, text2, j, cache), self.helper(text1, i, text2, j+1, cache))
            
        return cache[i][j]
