class Solution:

    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)
        if total % 3 != 0:
            False
        for i in range(1, len(A)):
            A[i] += A[i - 1]
        if total == 0 and A.count(0) < 3:
            return False
        return True if A.count(total // 3) and A.count(total // 3 * 2) and (A.index(total // 3) < len(A) - A[::-1].index(total // 3 * 2)) else False
