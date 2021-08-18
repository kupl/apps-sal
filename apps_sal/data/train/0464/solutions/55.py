class Solution:
    def minOperations(self, n: int) -> int:

        return sum([abs(n - 2 * i - 1) for i in range(n) if abs(n - 2 * i - 1) > 0]) // (2)
