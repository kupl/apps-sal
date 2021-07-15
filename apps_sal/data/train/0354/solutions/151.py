class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dfs(n, i, k):
            if not n: return 1
            ans = 0
            for j in range(6):
                if i != j:
                    ans += dfs(n-1, j, 1)
                elif k+1 <= rollMax[j]:
                    ans += dfs(n-1, j, k+1)
            return ans    
        
        return sum(dfs(n-1, i, 1) for i in range(6)) % 1000000007
