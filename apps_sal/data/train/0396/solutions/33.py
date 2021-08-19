class Solution:

    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0 or K % 5 == 0:
            return -1
        res = 1
        while res % K:
            res = 10 * res + 1
        return len(str(res))
