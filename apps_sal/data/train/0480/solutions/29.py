class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:

        def ncr(n, r, p):
            num = den = 1
            for i in range(r):
                num = num * (n - i) % p
                den = den * (i + 1) % p
            return num * pow(den, p - 2, p) % p
        ans = 0
        dp = [[0 for i in range(min(steps, arrLen))] for j in range(steps + 1)]
        dp[1][1] = 1
        for k in range(2, steps + 1):
            for l in range(len(dp[k])):
                (f, b) = (l - 1, l + 1)
                if f >= 0 and f < len(dp[k]):
                    dp[k][f] += dp[k - 1][l]
                if b >= 0 and b < len(dp[k]):
                    dp[k][b] += dp[k - 1][l]
        for numstay in range(0, steps + 1):
            numMoves = steps - numstay
            if numMoves % 2 != 0:
                continue
            ans += ncr(numstay + numMoves, numstay, 1000000007) * dp[numMoves][0] % 1000000007
            ans = ans % 1000000007
        return ans + 1
