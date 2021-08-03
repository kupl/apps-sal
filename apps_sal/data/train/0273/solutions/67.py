class Solution:
    def racecar(self, target: int) -> int:
        LIMIT = 2**(target.bit_length()) - 1
        dp = [0, 1, 4] + [float('INF')] * (LIMIT - 2)
        for t in range(3, target + 1):
            k = t.bit_length()
            if t == 2**k - 1:
                dp[t] = k
                continue
            # not cross t, but first reverse to position t - 2**(k-1) + 2**j, then reverse and accelerate to t
            for j in range(k):
                dp[t] = min(dp[t], dp[t - 2**(k - 1) + 2**j] + k + j + 1)
            # first cross t to 2**k - 1, then reverse to t
            dp[t] = min(dp[t], k + 1 + dp[2**k - 1 - t])

        return dp[target]
