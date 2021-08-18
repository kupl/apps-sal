class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        result = 0

        for i in range(0, N):
            x = (N - i * (i + 1) / 2) / (i + 1)
            if x <= 0:
                break

            if x % 1 == 0:
                result += 1

        return result
