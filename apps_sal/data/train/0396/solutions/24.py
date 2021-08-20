class Solution:

    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0 or K % 5 == 0:
            return -1
        n = 1
        length = 1
        while True:
            if int(n) % K == 0:
                return length
            n = n * 10 + 1
            length += 1
