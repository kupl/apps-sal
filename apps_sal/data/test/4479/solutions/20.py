class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:

        for i in range(K):
            min_ = min(A)
            idx = A.index(min_)
            A[idx] = -A[idx]
            max_ = sum(A)
        return max_
            

