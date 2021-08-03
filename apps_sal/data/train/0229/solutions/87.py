class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        c = collections.Counter(A)

        for x in sorted(A, key=abs):
            if c[x] == 0:
                continue
            if c[2 * x] == 0:
                return False
            c[x] -= 1
            c[2 * x] -= 1
        return True
