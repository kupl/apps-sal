import numpy as np


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        dp = np.diag(arr)

        for distance in range(1, n):
            for i in range(n - distance):
                if dp[i + distance - 1, i] <= dp[i + distance, i + distance]:
                    dp[i + distance, i] = dp[i + distance, i + distance]
                else:
                    dp[i + distance, i] = dp[i + distance - 1, i]

                if distance == 1:
                    minvalue = dp[i, i] * dp[i + distance, i + 1]
                else:
                    minvalue = dp[i, i] * dp[i + distance, i + 1] + dp[i + 1, i + distance]
                for j in range(1, distance):
                    if j == distance - 1:
                        tempvalue = dp[i + j, i] * dp[i + distance, i + j + 1] + dp[i, i + j]
                    else:
                        tempvalue = dp[i + j, i] * dp[i + distance, i + j + 1] + dp[i, i + j] + dp[i + j + 1, i + distance]
                    if tempvalue <= minvalue:
                        minvalue = tempvalue
                dp[i, i + distance] = minvalue
        return dp[0, n - 1]
