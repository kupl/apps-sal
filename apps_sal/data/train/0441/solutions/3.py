class Solution:

    def consecutiveNumbersSum(self, N: int) -> int:
        num_ways = 1
        n = 2
        while n * (n + 1) / 2 <= N:
            if (N - n * (n + 1) / 2) % n == 0:
                num_ways += 1
            n += 1
        return num_ways
