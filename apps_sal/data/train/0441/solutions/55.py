class Solution:

    def consecutiveNumbersSum(self, N: int) -> int:
        res = 0
        k = 1
        while N - k * (k + 1) // 2 >= 0:
            if (N - k * (k + 1) // 2) % k == 0:
                res += 1
            k += 1
        return res
