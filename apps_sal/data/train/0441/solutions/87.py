class Solution:

    def consecutiveNumbersSum(self, N: int) -> int:
        count = 0
        for i in range(1, int(math.sqrt(2 * N)) + 1):
            temp = (2 * N - i ** 2 + i) / 2 / i
            if temp > 0 and temp == int(temp):
                count += 1
        return count
