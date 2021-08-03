from typing import List
import numpy
import sys
import bisect


class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:

        tmp = 0
        n = len(stones)
        dims = (n, n)
        dp = numpy.zeros(dims)
        presum = numpy.zeros(n + 1)

        if (n - 1) % (K - 1) != 0:
            return -1

        for index, stone in enumerate(stones):
            tmp += stone
            presum[index + 1] = tmp

        for rlen in range(K, n + 1):
            for i in range(0, n - rlen + 1):
                end = i + rlen - 1
                dp[i][end] = sys.maxsize
                for j in range(i, end, K - 1):
                    dp[i][end] = min(dp[i][end], dp[i][j] + dp[j + 1][end])

                if (rlen - 1) % (K - 1) == 0:
                    dp[i][end] += presum[end + 1] - presum[i]

        return int(dp[0][n - 1])
