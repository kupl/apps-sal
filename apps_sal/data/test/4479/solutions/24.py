class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        
        max_sum = -999999
        for _ in range(K):
            A = sorted(A)
            min_index = A.index(min(A))
            
            A[min_index] = -A[min_index]

            max_ = sum(A)
            # print(max_)
            # max_sum = max(max_sum, max_)
        return max_
