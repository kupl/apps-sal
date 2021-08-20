import bisect


class Solution:

    def longestOnes(self, A: List[int], K: int) -> int:
        n = len(A)
        zeros = 0
        dp = [0] * n
        ans = 0
        for i in range(n):
            if A[i] == 0:
                zeros += 1
            dp[i] = zeros
        for i in range(n):
            val = dp[i]
            if A[i] == 1:
                right = bisect.bisect_left(dp, val + K + 1)
            else:
                right = bisect.bisect_left(dp, val + K)
            delta = right - i
            ans = max(ans, delta)
        return ans
