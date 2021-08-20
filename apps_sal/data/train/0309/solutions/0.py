from collections import Counter


class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        c = dict(Counter(A).most_common())
        m1 = max(c.values())
        index = {}
        dp = [[2] * len(A) for i in A]
        m = 2
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                a = A[i]
                c = A[j]
                b = 2 * a - c
                if b in index:
                    dp[i][j] = dp[index[b]][i] + 1
            index[A[i]] = i
            m = max(m, max(dp[i]))
        return max(m, m1)
