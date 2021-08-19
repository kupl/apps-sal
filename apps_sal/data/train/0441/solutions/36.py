class Solution:

    def consecutiveNumbersSum(self, N: int) -> int:
        ans = 0
        upper_limit = ceil((2 * N + 0.25) ** 0.5 - 0.5) + 1
        for x in range(1, upper_limit):
            if (2 * N - x * x + x) % (2 * x) == 0 and (2 * N - x * x + x) / (2 * x) > 0:
                ans += 1
        return ans
