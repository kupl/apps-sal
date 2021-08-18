class Solution:
    def minOperations(self, n: int) -> int:
        total = 0
        for i in range(n // 2):
            total += n - (2 * i + 1)
        return total

        return count
