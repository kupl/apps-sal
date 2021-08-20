from collections import defaultdict


class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        count = 2
        diff_map = defaultdict(dict)
        for i in range(len(A)):
            for j in range(0, i):
                diff = A[i] - A[j]
                diff_map[i][diff] = 1 + diff_map[j].get(diff, 1)
                count = max(count, diff_map[i][diff])
        return count
