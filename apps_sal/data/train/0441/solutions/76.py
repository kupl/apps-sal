class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        k = 1
        num_ways = 0
        floor = (N - k * (k - 1) // 2) // k
        while floor > 0:
            this_sum = (floor + k - 1) * (floor + k) // 2 - floor * (floor - 1) // 2
            if this_sum == N:
                num_ways += 1
            k += 1
            floor = (N - k * (k - 1) // 2) // k
        return num_ways
