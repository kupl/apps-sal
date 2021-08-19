class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        if len(A) < 3:
            return len(A)
        sub_lens = [{} for i in A]
        max_len = 0
        for i in range(0, len(A)):
            for j in range(0, i):
                diff = A[i] - A[j]
                sub_lens[i][diff] = max(sub_lens[i].get(diff, 1), sub_lens[j].get(diff, 1) + 1)
                max_len = max(max_len, sub_lens[i][diff])
        return max_len
