class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:

        max_sum = -999999
        for _ in range(K):
            A = sorted(A)
            min_index = A.index(min(A))

            A[min_index] = -A[min_index]

            max_ = sum(A)
        return max_
