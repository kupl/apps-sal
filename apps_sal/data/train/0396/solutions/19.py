class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0 or K % 5 == 0:
            return -1
        ans, N = 1, 1
        while N % K:
            N %= K
            N = N * 10 + 1
            ans += 1
        return ans
