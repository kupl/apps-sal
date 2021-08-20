class Solution:

    def maxJumps(self, A: List[int], d: int) -> int:
        dp = [1] * len(A)
        steps = [(v, i) for (i, v) in enumerate(A)]
        steps.sort()
        print(steps)
        for (val, i) in steps:
            maxVal = val
            for j in range(i + 1, min(i + d + 1, len(steps))):
                if A[j] > maxVal:
                    maxVal = max(maxVal, A[j])
                    dp[j] = max(dp[j], dp[i] + 1)
            maxVal = val
            for j in reversed(range(max(i - d, 0), i)):
                if A[j] > maxVal:
                    maxVal = max(maxVal, A[j])
                    dp[j] = max(dp[j], dp[i] + 1)
        print(dp)
        return max(dp)
