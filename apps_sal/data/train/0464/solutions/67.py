class Solution:
    def minOperations(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        else:
            return (int(n / 2)) + self.minOperations(n - 1)
