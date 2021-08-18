class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:

        length = 1
        p10 = 10
        N = 1

        if not K % 2:
            return -1

        if not K % 5:
            return -1

        while True:
            if not N % K:
                return length

            N += p10
            p10 *= 10
            length += 1
