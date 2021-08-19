class Solution:

    def canReorderDoubled(self, A: List[int]) -> bool:
        c = collections.Counter(A)
        for x in sorted(c):
            if c[x] == 0:
                continue
            if c[x] < 0:
                return False
            if x == 0:
                if c[x] % 2 != 0:
                    return False
                else:
                    continue
            if x > 0:
                temp = 2 * x
            elif x % 2:
                return False
            else:
                temp = x // 2
            if c[temp] < c[x]:
                return False
            else:
                c[temp] -= c[x]
        return True
