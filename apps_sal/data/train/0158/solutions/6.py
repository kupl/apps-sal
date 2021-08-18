
from functools import lru_cache


class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        n = len(A)

        @lru_cache(None)
        def dfs(s):
            if s == B:
                return 0
            idx = 0
            while s[idx] == B[idx]:
                idx += 1
            res = float('inf')
            for nxt in range(idx + 1, n):
                if s[nxt] != B[idx]:
                    continue
                res = min(res, dfs(s[:idx] + s[nxt] + s[idx + 1:nxt] + s[idx] + s[nxt + 1:]) + 1)
            return res
        return dfs(A)
