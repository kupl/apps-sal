class Solution:
    def minOperations(self, n: int) -> int:

        v = 0
        for i in range(n):
            v += 2 * i + 1

        mean = v // n

        ans = 0
        for i in range(n):
            ans += max(0, 2 * i + 1 - mean)
        return ans
