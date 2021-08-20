class Solution:

    def minOperations(self, a: List[int]) -> int:
        (ans, max_len) = (0, 0)
        for (i, x) in enumerate(a):
            b = bin(x)
            ans += b.count('1')
            max_len = max(max_len, len(b) - 2)
        return ans + max_len - 1
