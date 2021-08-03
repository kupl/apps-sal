class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        for i in range(K):
            A[0] = -1 * A[0]
            if A[0] > 0:
                A.sort()
        return sum(A)
