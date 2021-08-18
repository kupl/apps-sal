class Solution:
    def minOperations(self, n: int) -> int:

        if n <= 1:
            return 0
        else:
            ops = 0
            for x in range(n - 1, 0, -2):
                ops += x
            return ops
