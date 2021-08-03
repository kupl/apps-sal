class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        count = 0
        max_k = ceil((2 * N + 1 / 4) ** 0.5 - 0.5) + 1
        for k in range(1, max_k):
            if (N - k * (k + 1) / 2) % k == 0:
                count += 1
        return count
