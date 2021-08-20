class Solution:

    def leastOpsExpressTarget(self, x: int, target: int) -> int:

        def dp(i, j):
            if i == 0:
                return 2 * j
            if j == 1:
                return 2
            if (i, j) in memo:
                return memo[i, j]
            base = x ** i
            (q, r) = divmod(j, base)
            if r == 0:
                return q * i
            memo[i, j] = min(q * i + dp(i - 1, r), (q + 1) * i + dp(i - 1, base - r))
            return memo[i, j]
        memo = {}
        return dp(ceil(log(target, x)), target) - 1
