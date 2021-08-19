class Solution:

    def consecutiveNumbersSum(self, N: int) -> int:
        cnt = 0
        upper_limit = ceil((2 * N + 1 / 4) ** 0.5 - 0.5 + 1)
        for k in range(1, upper_limit):
            x = (2 * N - k ** 2 - k) / (2 * k)
            if int(x) == x and x >= 0:
                cnt += 1
        return cnt
