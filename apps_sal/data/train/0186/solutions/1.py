class Solution:

    def largestNumber(self, cost: List[int], target: int) -> str:

        @lru_cache(None)
        def dfs(c):
            if c == 0:
                return 0
            ans = -float('inf')
            for i in range(9):
                if cost[i] <= c:
                    ans = max(ans, 10 * dfs(c - cost[i]) + i + 1)
            return ans
        res = dfs(target)
        return str(res) if res > 0 else '0'


'\nclass Solution:\n    def largestNumber(self, cost: List[int], target: int) -> str:\n        from functools import lru_cache\n        @lru_cache(None)\n        def dfs(target):\n            if target == 0: return 0\n            res = -float("inf")\n            for i in range(len(cost)):\n                if cost[i] <= target:\n                    res = max(res, 10*dfs(target - cost[i])+i+1)\n            return res\n        res = dfs(target)\n        return str(res) if res > 0 else "0"\n'
