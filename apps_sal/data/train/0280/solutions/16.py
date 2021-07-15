from functools import lru_cache
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        @lru_cache(maxsize=None)
        def costs(i, j):
            if i>=j:
                return 0
            return costs(i+1,j-1)+(0 if s[i]==s[j] else 1)
        
        @lru_cache(maxsize=None)
        def dfs(j, k):
            if k==1:
                return costs(0,j)
            if k>j+1:
                return 0
            return min(dfs(i, k-1)+costs(i+1,j) for i in range(j))
        
        return dfs(len(s)-1, k)
