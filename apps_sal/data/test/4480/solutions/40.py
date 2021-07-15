class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        s = sum(A)
        if s % 3 != 0:
            return False
        s = s / 3
        t = 0
        count = 0
        for x in A:
            t += x
            if t == s:
                t = 0
                count += 1
        if t == 0 and count >= 3:
            return True
        else:
            return False
