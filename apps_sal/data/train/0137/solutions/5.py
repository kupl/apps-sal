class Solution:

    def minimumOneBitOperations(self, n: int) -> int:
        ans = 0
        while n > 0:
            ans = ans ^ n
            n = n >> 1
        return ans
