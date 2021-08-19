class Solution:

    def maximumSum(self, arr: List[int]) -> int:
        (ans, dp1, dp2, lr, rl) = (-math.inf, [None] * len(arr), [None] * len(arr), 0, 0)
        for (i, val) in enumerate(arr):
            (lr, rl) = (max(lr, 0) + val, max(rl, 0) + arr[len(arr) - 1 - i])
            (dp1[i], dp2[len(arr) - 1 - i]) = (lr, rl)
            ans = max(ans, lr, rl)
        for i in range(1, len(arr) - 1):
            if arr[i] < 0:
                ans = max(ans, dp1[i - 1] + dp2[i + 1])
        return ans
