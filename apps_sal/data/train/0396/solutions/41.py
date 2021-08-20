class Solution:

    def smallestRepunitDivByK(self, K: int) -> int:
        seen = set()
        remainder = 1
        N = 1
        i = 1
        while remainder % K != 0:
            N = N * 10 + 1
            remainder = N % K
            if remainder in seen:
                return -1
            seen.add(remainder)
            i += 1
        return i
