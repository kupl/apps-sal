class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        for i, a2 in enumerate(A[1:], start=1):  # enumerate start=1 index 起始數值
            for j, a1 in enumerate(A[:i]):
                d = a2 - a1
                if (j, d) in dp:
                    dp[i, d] = dp[j, d] + 1
                else:
                    dp[i, d] = 2  # 兩個數 構成一個d
        return max(dp.values())
