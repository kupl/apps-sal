class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        d = [{} for _ in range(len(A))]
        longest = 0
        for i in range(1, len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                d[i][diff] = max(d[i].get(diff, 0), 1 + d[j].get(diff, 1))
                longest = max(longest, d[i][diff])
        return longest
