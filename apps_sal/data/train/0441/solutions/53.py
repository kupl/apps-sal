class Solution:

    def consecutiveNumbersSum(self, N: int) -> int:
        k = 1
        num_ways = 0
        while k * (k - 1) // 2 < N:
            if (N - k * (k - 1) // 2) % k == 0:
                num_ways += 1
            k += 1
        return num_ways
