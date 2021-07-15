class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        counter = 0
        i = 0

        while N - (i * (i + 1) // 2) > 0:
            if (N - (i * (i + 1) // 2)) % (i + 1) == 0:
                counter += 1

            i += 1

        return counter
