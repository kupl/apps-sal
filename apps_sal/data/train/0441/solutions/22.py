class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        last_check = ceil(sqrt(2 * N))
        num_ways = 0
        for i in range(1, last_check):
            if (N * 2) % i == 0 and (i % 2 == 1 or (N * 2 / i) % 2 == 1):
                num_ways += 1
        return num_ways
