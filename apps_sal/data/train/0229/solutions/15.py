class Solution:

    def canReorderDoubled(self, A: List[int]) -> bool:
        pos = [x for x in A if x >= 0]
        neg = [x for x in A if x < 0]
        for L in (pos, neg):
            count = collections.Counter(L)
            for x in sorted(L, key=abs):
                if count[x] == 0:
                    continue
                if count[2 * x] == 0:
                    return False
                count[x] -= 1
                count[2 * x] -= 1
        return True
