class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        c = collections.Counter(A)
        cc = sorted(c, key=abs)
        # print(cc)
        for x in cc:
            # print(str(x), end=\": \")
            # print(c)
            if c[x] > c[2 * x]:
                return False
            c[2 * x] -= c[x]
        # print(c)
        return True
