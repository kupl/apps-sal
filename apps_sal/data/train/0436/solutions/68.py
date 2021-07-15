class Solution:
    def minDays(self, n: int) -> int:
        return self.dfs(n)
    
    @lru_cache(None)
    def dfs(self, n):
        if n < 2:
            return n
        if n < 0:
            return -1
        ans = sys.maxsize
        if n % 3 == 0:
            ans = min(1 + self.dfs(n // 3), ans)
        if n % 2 == 0:
            ans = min(1 + self.dfs(n // 2), ans)
        if (n - 1) % 3 == 0 or (n - 1) % 2 == 0:
            ans = min(1 + self.dfs(n - 1), ans)
        if (n - 2) % 3 == 0:
            ans = min(2 + self.dfs(n - 2), ans)
        return ans
