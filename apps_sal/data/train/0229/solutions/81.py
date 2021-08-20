class Solution:

    def canReorderDoubled(self, A: List[int]) -> bool:
        B = []
        for x in A:
            if x > 0:
                B.append(x)
            else:
                B.append(-x)
        count = collections.Counter(B)
        for x in sorted(B):
            if count[x] == 0:
                continue
            if count[2 * x] == 0:
                return False
            else:
                count[x] -= 1
                count[2 * x] -= 1
        return True
