class Solution:
    def soupServings(self, N: int) -> float:
        if N > 10000:
            return 1
        
        rounds = (N + 25 - 1) // 25
        dp = [{(N, N): 1}] + [collections.defaultdict(float) for _ in range(rounds)]
        for i in range(1, rounds + 1):
            for a, b in dp[i-1]:
                if a <= 0 or b <= 0:
                    dp[i][a, b] += dp[i-1][a, b]
                else:
                    dp[i][max(a-100, 0), b] += dp[i-1][a, b] * 0.25
                    dp[i][max(a-75, 0), max(b-25, 0)] += dp[i-1][a, b] * 0.25
                    dp[i][max(a-50, 0), max(b-50, 0)] += dp[i-1][a, b] * 0.25
                    dp[i][max(a-25, 0), max(b-75, 0)] += dp[i-1][a, b] * 0.25
        
        res = dp[rounds][0, 0] / 2
        for a, b in dp[rounds]:
            if a <= 0 and b > 0:
                res += dp[rounds][a,b]
        return res
