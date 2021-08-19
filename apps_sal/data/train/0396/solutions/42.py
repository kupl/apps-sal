class Solution:

    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0 or K % 5 == 0:
            return -1
        l = len(str(K))
        n = 1
        for i in range(1, l):
            n = n * 10 + 1
        while True:
            if n % K == 0:
                return len(str(n))
            n = n * 10 + 1
        return -1
