class Solution:

    def smallestRepunitDivByK(self, K: int) -> int:
        n = 0
        if K % 2 == 0:
            return -1
        for i in range(0, K + 1):
            n = n * 10 + 1
            if n % K == 0:
                print((n, K, i))
                return i + 1
        return -1
