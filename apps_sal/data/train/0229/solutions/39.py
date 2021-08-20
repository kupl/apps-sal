class Solution:

    def canReorderDoubled(self, A: List[int]) -> bool:
        c = collections.Counter(A)
        cc = sorted(c, key=abs)
        for x in cc:
            if c[x] > c[2 * x]:
                return False
            c[2 * x] -= c[x]
        return True
