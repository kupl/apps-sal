class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0 or K % 5 == 0:
            return -1

        N = 1
        result = 1

        while N % K:
            N %= K
            result += 1
            N = N * 10 + 1
        return result
