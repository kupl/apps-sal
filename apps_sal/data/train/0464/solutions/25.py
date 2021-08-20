class Solution:

    def minOperations(self, n: int) -> int:
        ops = 0
        for i in range(n):
            ops += abs(2 * i + 1 - n)
        return ops // 2
