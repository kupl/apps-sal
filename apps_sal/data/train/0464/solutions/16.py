

class Solution:
    def minOperations(self, n: int) -> int:
        mid_point = (2 * (n // 2)) + 1 - (n % 2 == 0)
        return sum([mid_point - ((2 * i) + 1) for i in range(n // 2)])
