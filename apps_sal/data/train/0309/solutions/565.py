class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        pos_diff_to_length = {}
        result = 0
        for i in range(1, len(A)):
            for j in range(i):
                if (j, A[i] - A[j]) in pos_diff_to_length:
                    pos_diff_to_length[i, A[i] - A[j]] = pos_diff_to_length[j, A[i] - A[j]] + 1
                else:
                    pos_diff_to_length[i, A[i] - A[j]] = 2
                result = max(result, pos_diff_to_length[i, A[i] - A[j]])
        return result
