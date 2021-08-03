from typing import List

import numpy


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        result = 0
        dims = (n + 1, 7)
        dp = numpy.zeros(dims, dtype=int)
        sums = [0] * (n + 1)
        kMod = 10 ** 9 + 7
        for j in range(0, 6):
            dp[1][j] = 1
            sums[1] += dp[1][j]

        for i in range(2, n + 1):
            for j in range(6):
                k = i - rollMax[j]
                if k <= 1:
                    invalid = max(k, 0)
                else:
                    invalid = sums[k - 1] - dp[k - 1][j]

                dp[i][j] = ((sums[i - 1] - invalid) % kMod + kMod) % kMod
                sums[i] = (sums[i] + dp[i][j]) % kMod
                pass
            pass

        return sums[-1]
