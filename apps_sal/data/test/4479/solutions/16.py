class Solution:

    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        for x in range(K):
            minNum = A.index(min(A))
            A[minNum] = A[minNum] * -1
        return sum(A)
