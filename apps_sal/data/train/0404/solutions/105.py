class Solution:

    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        dp = [[A[0] if k == 1 else 0 for k in range(K + 1)]]
        for (count, i) in enumerate(range(1, len(A))):
            dp.append([0])
            dp[i].append((dp[i - 1][1] * (count + 1) + A[i]) / (count + 2))
        for i in range(1, len(A)):
            for k in range(2, K + 1):
                val = float('-inf')
                _sum = 0
                for j in range(i, 0, -1):
                    _sum += A[j]
                    val = max(dp[j - 1][k - 1] + _sum / (i - j + 1), val)
                dp[i].append(val)
        return dp[len(A) - 1][K]
