class Solution:

    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        s = sum(A)
        if s % 3 != 0:
            return False
        x = s // 3
        c = 0
        d = 0
        for a in A[:-1]:
            c += a
            if d == 0 and c == x:
                d = 1
            elif d == 1 and c == 2 * x:
                return True
        return False
