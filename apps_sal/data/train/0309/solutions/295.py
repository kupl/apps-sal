from collections import defaultdict

class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        mx = 0
        dp = [defaultdict(int) for _ in range(len(A))]
        for i,a in enumerate(A):
            for j,b in enumerate(A[:i]):
                if a - b in dp[j].keys():
                    dp[i][a-b] = dp[j][a-b] + 1
                else:
                    dp[i][a-b] = 2
                mx = max(mx, dp[i][a-b])
        return mx
