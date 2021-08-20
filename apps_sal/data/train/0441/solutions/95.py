class Solution:

    def consecutiveNumbersSum(self, N: int) -> int:
        (count, i) = (1, 2)
        while i < sqrt(2 * N):
            if (N - (i ** 2 - i) / 2) % i == 0:
                count += 1
            i += 1
        return count
