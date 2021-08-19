class Solution:

    def consecutiveNumbersSum(self, N: int) -> int:
        count = 0
        i = 1
        while i ** 2 + i <= 2 * N:
            temp = N / i - (i - 1) / 2
            if int(temp) == temp:
                count += 1
            i += 1
        return count
