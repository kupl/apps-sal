class Solution:

    def consecutiveNumbersSum(self, N: int) -> int:
        (res, k) = (0, 1)
        while k * (k + 1) <= 2 * N:
            x = float(N) / k - (k + 1) / 2.0
            if 2 * N % k == 0 and x.is_integer():
                res += 1
            k += 1
        return res
