class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K == 1:
            return 1
        mod= 1
        for length in range(2, K + 1):
            mod = (10 * mod + 1) % K
            if mod == 0: return length
        return -1
