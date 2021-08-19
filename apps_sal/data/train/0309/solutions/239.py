from collections import defaultdict


class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        count = defaultdict(lambda: 1)
        n = len(A)
        for i in range(n):
            for j in range(i + 1, n):
                count[j, A[j] - A[i]] = count[i, A[j] - A[i]] + 1
        return max(count.values())
