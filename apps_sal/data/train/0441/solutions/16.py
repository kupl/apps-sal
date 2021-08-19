class Solution:

    def consecutiveNumbersSum(self, N: int) -> int:
        (count, upper_limit) = (0, int(math.sqrt(2 * N + 1 / 4) - 1 / 2))
        for i in range(1, upper_limit + 1):
            N -= i
            if not N % i:
                count += 1
        return count
