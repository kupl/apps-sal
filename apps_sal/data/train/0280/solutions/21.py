from functools import lru_cache


class Solution:

    def palindromePartition(self, s: str, k: int) -> int:

        @lru_cache(None)
        def check(x):
            ans = 0
            for i in range(len(x) // 2):
                if x[i] != x[-1 - i]:
                    ans += 1
            return ans

        @lru_cache(None)
        def dfs(start, num):
            if num == 1:
                return check(s[start:])
            res = float('inf')
            for i in range(start + 1, len(s)):
                res = min(res, check(s[start:i]) + dfs(i, num - 1))
            return res
        return dfs(0, k)
