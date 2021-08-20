class Solution:

    def consecutiveNumbersSum(self, N: int) -> int:
        ans = 0
        for i in range(1, N + 1):
            x = (2 * N / i - i + 1) / 2
            if x <= 0:
                break
            if x == int(x):
                ans += 1
        return ans
