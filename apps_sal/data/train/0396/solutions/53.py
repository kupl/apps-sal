class Solution:

    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0 or K % 5 == 0:
            return -1
        n = 0
        seen = set()
        for i in range(K):
            n *= 10
            n += 1
            m = n % K
            if m == 0:
                return i + 1
            elif m in seen:
                return -1
            seen.add(m)
        return -1
