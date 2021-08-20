class Solution:

    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        if K == 1:
            return sum(A)
        dp = [0] * (len(A) + 1)
        for i in range(1, len(A) + 1):
            cand = []
            for j in range(1, K + 1):
                if j > i:
                    break
                temp = dp[i - j] + max(A[i - j:i]) * j
                cand.append(temp)
            dp[i] = max(cand)
        print(dp)
        return dp[-1]
