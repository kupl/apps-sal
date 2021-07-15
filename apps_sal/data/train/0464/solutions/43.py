class Solution:
    def minOperations(self, n: int) -> int:
        half = n//2
        return half*n - half**2
