class Solution:

    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 10 not in (1, 3, 7, 9):
            return -1
        n = 1
        for i in range(1, K + 1):
            if n % K == 0:
                return i
            else:
                n = n * 10 + 1
        return -1
