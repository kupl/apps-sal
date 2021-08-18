class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:

        n = 1
        count = 0
        while N > n * (n - 1) // 2:
            if (N - n * (n - 1) // 2) % n == 0:
                count += 1
            n += 1

        return count
