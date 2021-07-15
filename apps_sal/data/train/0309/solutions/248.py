class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        # find step between number, and count max of consequence index.
        # step: [arr], # preserve order?
        
        if not A:
            return 0
        if len(A) == 2:
            return 2
        
        dp = [{} for a in range(len(A))]
        max_len = 0
        for i in range(1, len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                if diff in dp[j]:
                    dp[i][diff] = max(2, 1+dp[j][diff])
                else:
                    dp[i][diff] = 2
                max_len = max(max_len, dp[i][diff])
        return max_len
