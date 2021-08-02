class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        s = 0
        res = 0
        s1 = sum(A)
        if s1 % 3 != 0:
            return False
        target = s1 // 3
        for a in A:
            s += a
            if s == target:
                s = 0
                res += 1
        return res > 2
