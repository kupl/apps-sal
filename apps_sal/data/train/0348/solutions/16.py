class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        # minimum size is > 1
        # do two array, positive and negative
        ans, dp1, dp2, lr, rl = -math.inf, [None] * len(arr), [None] * len(arr), 0, 0
        for i, val in enumerate(arr):
            lr, rl = max(lr, 0) + val, max(rl, 0) + arr[len(arr) - 1 - i]
            dp1[i], dp2[len(arr) - 1 - i] = lr, rl
            ans = max(ans, lr, rl)

        for i in range(1, len(arr) - 1):
            if arr[i] < 0:
                ans = max(ans, dp1[i - 1] + dp2[i + 1])
        return ans

    # def maximumSum(self, arr: List[int]) -> int:
    #     n = len(arr)
    #     max_ending_here0 = n * [arr[0]]  # no deletion
    #     max_ending_here1 = n * [arr[0]]  # at most 1 deletion
    #     for i in range(1, n):
    #         max_ending_here0[i] = max(max_ending_here0[i-1] + arr[i], arr[i])
    #         max_ending_here1[i] = max(max_ending_here1[i-1] + arr[i], arr[i])
    #         if i >= 2:
    #             max_ending_here1[i] = max(max_ending_here1[i], max_ending_here0[i-2] + arr[i])
    #     return max(max_ending_here1)
