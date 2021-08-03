class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)
        isum = 0

        for i in range(0, len(A) - 2):
            isum += A[i]
            if isum == total / 3:
                jsum = 0
                for j in range(i + 1, len(A) - 1):
                    jsum += A[j]
                    if isum == jsum == total - isum - jsum:
                        return True
        return False
