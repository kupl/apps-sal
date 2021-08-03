class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        while K != 0:
            A[A.index(min(A))] = -min(A)
            K -= 1
        return(sum(A))
