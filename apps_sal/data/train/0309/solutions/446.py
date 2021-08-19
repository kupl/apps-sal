from collections import defaultdict


class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        largestLen = 0
        longestArithSequence = [defaultdict(lambda: 1) for _ in range(len(A))]
        for i in range(1, len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                seqLen = longestArithSequence[i][diff] = max(longestArithSequence[i][diff], longestArithSequence[j][diff] + 1)
                largestLen = max(largestLen, seqLen)
        return largestLen
