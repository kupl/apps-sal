class Solution:

    def canReorderDoubled(self, A: List[int]) -> bool:
        D1 = collections.Counter()
        D2 = collections.Counter()
        zero = 0
        for a in A:
            if a < 0:
                D1[a] += 1
            else:
                D2[a] += 1
        for d in sorted(D1, reverse=1):
            if D1[d]:
                if D1[d * 2] < D1[d]:
                    return False
                D1[d * 2] -= D1[d]
        for d in sorted(D2):
            if D2[d]:
                if D2[d * 2] < D2[d]:
                    return False
                D2[d * 2] -= D2[d]
        return True
