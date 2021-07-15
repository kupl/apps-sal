class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        total = len(stones)
        if (total-1) % (K-1):
            return -1
        
        
        prefix = [0] * (total+1)
        for i in range(total):
            prefix[i+1] = prefix[i]+stones[i]
        
        import functools
        @functools.lru_cache(None)
        def dfs(i, j):
            if j-i+1 < K:
                return 0
            res = min(dfs(i,k)+dfs(k+1,j) for k in range(i, j, K-1))
            if (j-i) % (K-1) == 0:
                res += prefix[j+1]-prefix[i]
                
            return res
        
        return dfs(0, total-1)
