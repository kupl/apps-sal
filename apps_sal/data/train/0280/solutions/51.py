class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        if n == k:
            return 0

        # @lru_cache(None)
        def cost(s):  # calculate the cost of transferring one substring into palindrome string
            r = 0
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    r += 1
                i += 1
                j -= 1
            return r

        @lru_cache(None)
        def dfs(s, k):
            if len(s) == k:
                return 0
            if k == 1:
                return cost(s)
            res = float('inf')
            for i in range(1, len(s)):
                res = min(res, cost(s[:i]) + dfs(s[i:], k - 1))
            return res
        return dfs(s, k)
