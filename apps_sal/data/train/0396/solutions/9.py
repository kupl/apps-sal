class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if not K % 2 or not K % 5:
            return -1
        # dic = {}
        r = 0
        for i in range(1, K + 1):
            r = (10 * r + 1) % K
            if not r % K:
                return i
