class Solution:

    def minOperations(self, n: int) -> int:
        c = 0
        for i in range(n // 2):
            c += n - (2 * i + 1)
        return c
