class Solution:

    def consecutiveNumbersSum(self, N: int) -> int:
        count = 0
        upper_limit = ceil((2 * N + 0.25) ** 0.5 - 0.5) + 1
        for k in range(1, upper_limit):
            if (N - k * (k + 1) // 2) % k == 0:
                count += 1
        return count
