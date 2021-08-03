from math import comb


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = {}
        for i in range(N + 1):
            dp[(i, 0)] = 0
        for k in range(1, K + 1):
            dp[(1, k)] = 1
        for k in range(1, K + 1):
            for n in range(2, N + 1):
                dp[(n, k)] = 1 + dp[(n - 1), k] + dp[(n - 1), k - 1]
        num = 1
        while dp[(num, K)] < N:
            num += 1
        return num
