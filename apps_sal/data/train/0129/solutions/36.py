class Solution:

    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        i_sum = [0] * len(A)
        j_sum = [0] * len(A)
        for i in range(len(A)):
            i_sum[i] = A[i] + i
        i_sum[-1] = 0
        for j in range(len(A)):
            j_sum[j] = A[j] - j
        print(j_sum)
        prefix_sum = [-float('inf')] * len(A)
        for j in range(len(A) - 2, -1, -1):
            prefix_sum[j] = max(j_sum[j + 1], prefix_sum[j + 1])
        max_sum = -float('inf')
        for i in range(len(A)):
            max_sum = max(max_sum, prefix_sum[i] + i_sum[i])
        print(prefix_sum)
        return max_sum
