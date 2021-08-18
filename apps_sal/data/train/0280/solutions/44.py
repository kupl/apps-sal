class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        memo = dict()

        def cost(s, i, j):
            ans = 0
            while i < j:
                if s[i] != s[j]:
                    ans += 1
                i += 1
                j -= 1
            return ans

        def dfs(i, k):
            if (i, k) in memo:
                return memo[(i, k)]
            if n - i == k:
                return 0
            if k == 1:
                return cost(s, i, n - 1)
            res = float('inf')
            for j in range(i, n - k + 1):
                res = min(res, cost(s, i, j) + dfs(j + 1, k - 1))
            memo[(i, k)] = res
            return res
        return dfs(0, k)
