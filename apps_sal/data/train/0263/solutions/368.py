class Solution:
    def knightDialer(self, n: int) -> int:
        
        moves = {1:[6, 8], 2:[7, 9], 3:[4, 8], 4:[0, 3, 9], 5:[], 6:[0, 1, 7], 7:[2, 6], 8:[1, 3], 9:[2, 4], 0:[4, 6]}
        
        from functools import lru_cache
        @lru_cache(maxsize = None)
        def dfs(i, length):
            if n == length:
                return 1
            
            total = 0
            for newI in moves[i]:
                total += dfs(newI, length + 1)
            return total
        
        ans = 0
        for i in range(0, 10):
            ans += dfs(i, 1)
            if ans >= 10**9+7:
                ans = ans%(10**9+7)
        return ans
