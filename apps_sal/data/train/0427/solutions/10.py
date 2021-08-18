class Solution:
    def countOrders(self, n: int) -> int:

        mod = 10**9 + 7
        facts = [1]
        for i in range(1, n + 1):
            facts.append(facts[-1] * i)

        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for p in range(n + 1):
            for d in range(n - p + 1):
                if p > 0 and d > 0:
                    dp[p][d] += ((dp[p - 1][d + 1] * p) % mod)
                    dp[p][d] += ((dp[p][d - 1] * d) % mod)
                elif p > 0 and d == 0:
                    dp[p][d] += ((dp[p - 1][d + 1] * p) % mod)
                elif d > 0 and p == 0:
                    dp[p][d] += (facts[d] % mod)
        return dp[n][0]
