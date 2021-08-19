class Solution:

    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0:
            return -1
        i = 1
        l = 1
        while i < K:
            i = i * 10 + 1
            l += 1
        residue = set()
        while True:
            r = i % K
            if r == 0:
                return l
            if r in residue:
                return -1
            residue.add(r)
            i = 10 * i + 1
            l += 1
