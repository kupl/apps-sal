class Solution:
    def minOperations(self, n: int) -> int:
        return sum(list(range(1, n, 2))) if n % 2 == 0 else sum(list(range(2, n, 2)))
