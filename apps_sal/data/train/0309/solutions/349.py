class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        mapping = {}
        n = len(A)
        if n < 2:
            return n
        max_ = 0
        for i in range(n):
            mapping[i] = {}
            for j in range(i):
                diff = A[i] - A[j]
                if diff not in mapping[j]:
                    mapping[i][diff] = 2
                else:
                    mapping[i][diff] = mapping[j][diff] + 1
                max_ = max(max_, mapping[i][diff])
        return max_
