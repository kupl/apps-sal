class Solution:

    def consecutiveNumbersSum(self, N: int) -> int:
        (c, k) = (0, 0)
        while k * (k + 1) / 2 < N:
            r = N - k * (k + 1) / 2
            if r % (k + 1) == 0:
                c += 1
            k += 1
        return c
