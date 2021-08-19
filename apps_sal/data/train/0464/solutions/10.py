class Solution:

    def minOperations(self, n: int) -> int:
        (i, ans) = (1, 0)
        while i < n:
            ans += n - i
            i += 2
        return ans
