class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        count = 0
        limit = ceil(sqrt(2 * N + 0.25) - 0.5)
        for k in range(1, limit + 1):
            if (N - k * (k + 1) // 2) % k == 0:
                count += 1
        return count
