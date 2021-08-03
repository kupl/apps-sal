class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        c = collections.Counter(A)
        for k in sorted(c, key=abs):
            if c[k] > c.get(2 * k, 0):
                return False
            c[2 * k] -= c[k]

        return True
