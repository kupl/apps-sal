class Solution:
    def minOperations(self, n: int) -> int:
        count = 0
        for i in range(n // 2):
            count += n - (2 * i + 1)
        return count
