class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        dp0, dp1, res = arr[0], 0, arr[0]
        for i in range(1, n):
            dp0, dp1 = max(dp0 + arr[i], arr[i]), max(dp0, dp1 + arr[i])
            res = max(dp0, dp1, res)
        return res
