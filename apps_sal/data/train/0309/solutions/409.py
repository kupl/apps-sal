class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        if len(A) <= 2:
            return len(A)
        idx_diff_to_longest = {}
        longest = 0
        for i in range(1, len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                prev_len = idx_diff_to_longest[(j, diff)] if (j, diff) in idx_diff_to_longest else 1
                idx_diff_to_longest[(i, diff)] = prev_len + 1
                longest = max(longest, prev_len + 1)
        return longest
