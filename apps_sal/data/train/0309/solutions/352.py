from collections import defaultdict


class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        d = defaultdict(dict)
        ans = 0
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                diff = A[j] - A[i]
                if diff in d[i]:
                    d[j][diff] = d[i][diff] + 1
                else:
                    d[j][diff] = 1
                ans = max(ans, d[j][diff])
        return ans + 1
