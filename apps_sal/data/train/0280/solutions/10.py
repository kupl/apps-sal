class Solution:
    def palindromePartition(self, s: str, k: int) -> int:

        @lru_cache(None)
        def dfs(subs, k):
            if k == len(subs):
                return 0
            if k == 1:
                return sum(subs[i] != subs[-1 - i] for i in range(len(subs) // 2))
            res = float('inf')
            for i in range(1, len(subs) - k + 2):
                res = min(res, dfs(subs[:i], 1) + dfs(subs[i:], k - 1))
            return res
        return dfs(s, k)
