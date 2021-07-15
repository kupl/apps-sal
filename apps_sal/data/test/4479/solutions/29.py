class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        while K>0:
            K-=1
            A[A.index(min(A))]=-min(A)
        return sum(A)
