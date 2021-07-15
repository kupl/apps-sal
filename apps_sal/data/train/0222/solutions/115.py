class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        n = len(A)
        two_sum = {}       
        result = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                curr_pair = (A[i], A[j])
                prev_pair = (A[j] - A[i], A[i])
                two_sum[curr_pair] = 2
                if prev_pair in two_sum:
                    two_sum[curr_pair] = max(two_sum[curr_pair], two_sum[prev_pair] + 1)
                    result = max(result, two_sum[curr_pair])
        return result
