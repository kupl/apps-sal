class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:

        long_len_sub_at_pos = {}

        for i in range(len(A)):
            for j in range(i):
                diff = A[i] - A[j]

                sub_len_at_j = long_len_sub_at_pos.get((diff, j), 1)
                long_len_sub_at_pos[(diff, i)] = max(long_len_sub_at_pos.get((diff, i), 0), sub_len_at_j + 1)

        return max(long_len_sub_at_pos.values())
