from collections import defaultdict

class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        # lengths (i, d) longest arithmetic subsequence starting at i
        # with difference d
        lengths = defaultdict(lambda: 1)
        
        for i in range(len(A) - 2, -1, -1):
            for j in range(len(A) - 1, i, -1):
                lengths[i, A[j] - A[i]] = lengths[j, A[j] - A[i]] + 1
        return max(lengths.values())
