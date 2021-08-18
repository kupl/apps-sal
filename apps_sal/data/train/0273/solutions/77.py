class Solution:
    def __init__(self):
        self._dp = {0: 0}

    def racecar(self, target):
        if target == 0:
            return 0
        if target == 1:
            return 1
        if target == 2:
            return 4
        dp = [2 ** 31 - 1] * (target + 1)
        dp[0], dp[1], dp[2] = 0, 1, 4
        for t in range(3, target + 1):
            k = t.bit_length()
            if t == 2 ** k - 1:
                dp[t] = k
                continue

            for m in range(k - 1):
                dp[t] = min(dp[t], dp[t - 2 ** (k - 1) + 2 ** m] + k - 1 + m + 2)

            if 2 ** k - 1 - t > 0:
                dp[t] = min(dp[t], dp[2 ** k - 1 - t] + k + 1)
        return dp[target]
