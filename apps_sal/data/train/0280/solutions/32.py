class Solution:

    def palindromePartition(self, s: str, k: int) -> int:
        memo = dict()
        n = len(s)

        def find_cost(l, r):
            cost = 0
            while l < r:
                if s[l] != s[r]:
                    cost += 1
                l += 1
                r -= 1
            return cost

        def dp(i, k):
            if (i, k) in memo:
                return memo[i, k]
            if n - i == 1:
                return 0
            if k == 1:
                return find_cost(i, n - 1)
            memo[i, k] = float('inf')
            for j in range(i + 1, n - k + 2):
                memo[i, k] = min(memo[i, k], find_cost(i, j - 1) + dp(j, k - 1))
            return memo[i, k]
        return dp(0, k)
