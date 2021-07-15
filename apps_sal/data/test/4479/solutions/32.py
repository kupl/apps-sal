class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        for i in range(K):
            A[A.index(min(A))] *= -1
            
        return sum(A)

