class Solution:

    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        s = sum(A)
        if s % 3 != 0:
            return False
        (curr, target) = (0, s // 3)
        count = 0
        for ix in range(len(A)):
            curr += A[ix]
            if curr == target:
                curr = 0
                count += 1
            if count == 2 and ix < len(A) - 1:
                return True
        return False
