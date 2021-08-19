class Solution:

    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        t = sum(A)
        if t % 3 != 0:
            return False
        s = 0
        p = 0
        for i in range(len(A)):
            s += A[i]
            if s == t // 3:
                s = 0
                p += 1
        if p >= 3:
            return True
        return False
