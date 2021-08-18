class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        memo = {}

        def cost(s, i, j):
            r = 0
            while i < j:
                if s[i] != s[j]:
                    r += 1
                i += 1
                j -= 1
            return r

        def dfs(i, k):
            if (i, k) in memo:
                return memo[(i, k)]
            if n - i == k:
                return 0
            if k == 1:
                return cost(s, i, n - 1)
            res = float('inf')
            for j in range(i + 1, n - k + 2):
                res = min(res, dfs(j, k - 1) + cost(s, i, j - 1))
            memo[(i, k)] = res
            return res
        return dfs(0, k)
