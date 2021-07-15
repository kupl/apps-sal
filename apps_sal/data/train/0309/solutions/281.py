class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        # dp[i][d] = longestArithSeqLength(A[:i]) with difference d
        # dp[i][d] = max(1 + dp[j][A[i]-A[j]] for j=[0..i-1])
        # n^2
        dp = dict()
        max_len = 0
        # [3,6,9,12]
        # {1: {3: 2}, 2: {6: 2, 3: 3}, 3: {9: 2, 6: 2, 3: 4}}
        # d = 3
        for i in range(len(A)):
            # dp[i] = {diff: max_len}
            dp[i] = dict()
            for j in range(i):
                d = A[i]-A[j]
                if d in dp[j]:
                    dp[i][d] = max(dp[i][d], 1 + dp[j][d]) if d in dp[i] else 1 + dp[j][d]
                else:
                    dp[i][d] = 2
                max_len = max(max_len, dp[i][d])
    
        return max_len

