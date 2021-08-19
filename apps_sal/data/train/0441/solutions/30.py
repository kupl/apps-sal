class Solution:

    def consecutiveNumbersSum(self, N: int) -> int:
        count = 1
        upper_limit = ceil((2 * N + 1) ** 0.5)
        for k in range(2, upper_limit):
            if (N - k * (k - 1) // 2) % k == 0:
                count += 1
        return count
