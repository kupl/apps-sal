class Solution:

    def minOperations(self, n: int) -> int:
        if n % 2 == 0:
            return n // 2 * (n // 2)
        else:
            return (n - 1) * (1 + (n - 1) // 2) // 2
