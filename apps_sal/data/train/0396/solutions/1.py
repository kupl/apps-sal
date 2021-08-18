class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:

        if K % 10 not in [1, 3, 7, 9]:
            return -1
        m = 0
        for d in range(1, K + 1):
            m = (m * 10 + 1) % K
            if not m:
                return d
        return -1
