class Solution:

    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0:
            return -1
        if K % 5 == 0:
            return -1
        ones = 1
        while ones % K != 0:
            ones = ones * 10 + 1
        return len(str(ones))
