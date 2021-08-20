class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        dp = collections.defaultdict(dict)
        max_val = 0
        for i in range(n):
            for j in range(i):
                dif = A[i] - A[j]
                dp[dif].setdefault(i, 0)
                dp[dif][i] = max(dp[dif][i], dp[dif].get(j, 0) + 1)
                max_val = max(dp[dif][i], max_val)
        return max_val + 1
