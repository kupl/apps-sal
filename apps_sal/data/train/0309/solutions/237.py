class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        idx_diff_count = {}
        for i in range(1,len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                if (j,diff) in idx_diff_count:
                    idx_diff_count[i,diff] = idx_diff_count[j,diff] + 1
                else:
                    idx_diff_count[i,diff] = 2
        return max(idx_diff_count.values())
