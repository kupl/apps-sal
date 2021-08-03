class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        c = 0

        while c < K:
            c += 1
            min_ = min(A)
            index = A.index(min_)
            A[index] = -1 * min_

        return sum(A)
