class Solution:
    def numPermsDISequence(self, S: str) -> int:
        from functools import lru_cache
        MOD = 10**9 + 7
        N = len(S)
        
        @lru_cache(None)
        def search(i, j):
            
            if not 0 <= j <= i:
                return 0
            
            if i == 0:
                return 1
            
            if S[i-1] == 'D':
                return (search(i, j+1) + search(i-1, j)) % MOD
            else:
                return (search(i, j-1) + search(i-1, j-1)) % MOD
            
        
        return sum(search(N, j) for j in range(len(S)+1)) % MOD
