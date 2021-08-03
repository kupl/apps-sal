class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0 or K % 5 == 0:
            return -1
        n = 0
        for i in range(100000):
            n *= 10
            n += 1
            if n % K == 0:
                return i + 1
        return -1
