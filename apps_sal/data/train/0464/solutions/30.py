class Solution:
    def minOperations(self, n: int) -> int:
        totalSum = int(n * (2 * 1 + (n - 1) * 2) / 2)
        targetNumber = int(totalSum / n)
        return sum(abs(2 * i + 1 - targetNumber) for i in range(0, n)) // 2
