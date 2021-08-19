# [Runtime: 4284 ms, faster than 10.74%] DP
# O(N^2)
# NOTE: diff can be either positive or negative
# f[i]: the longest length of arithmetic subsequences who takes A[i] as the tail.
#f[i] = defaultdict(lambda: 1)
# f[i] = {diff: longest length}
# f[i] = max(f[i][d], f[j][d] += 1) for j < i and d:=A[i]-A[j]
from collections import defaultdict


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = [defaultdict(lambda: 1) for _ in range(len(A))]
        for i, a in enumerate(A):
            for j in range(i):
                diff = A[i] - A[j]
                if dp[i][diff] < dp[j][diff] + 1:
                    dp[i][diff] = dp[j][diff] + 1
        return max(max(lens.values()) for lens in dp)
