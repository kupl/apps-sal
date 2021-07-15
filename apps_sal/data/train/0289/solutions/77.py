class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        N = len(A)
        
        # generate prefix sum array
        prefix = [0] * (N + 1)
        for i in range(1, N + 1):
            prefix[i] = prefix[i - 1] + A[i - 1]
            
        max_sum = 0
        for end_l in range(L, N + 1):
            start_l = end_l - L
            sum1 = prefix[end_l] - prefix[start_l]
            
            for end_m in range(M, start_l):
                sum2 = prefix[end_m] - prefix[end_m - M]
                max_sum = max(max_sum, sum1 + sum2)
            for start_m in range(end_l, N - M + 1):
                sum2 = prefix[start_m + M] - prefix[start_m]
                max_sum = max(max_sum, sum1 + sum2)
            
        return max_sum
