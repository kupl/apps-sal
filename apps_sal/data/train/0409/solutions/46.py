class Solution:

    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        if max(arr) <= 0:
            return 0
        if sum(arr) > 0:
            res = sum(arr) * (k - 2)
            dp = [0] * len(arr)
            dp[0] = arr[0]
            for i in range(1, len(arr)):
                dp[i] = dp[i - 1] + arr[i]
            res += max(dp)
            dp = [0] * len(arr)
            dp[-1] = arr[-1]
            for i in range(len(arr) - 2, -1, -1):
                dp[i] = dp[i + 1] + arr[i]
            res += max(dp)
            return res % (10 ** 9 + 7)
        (cur, res) = (0, 0)
        arr = arr + arr
        for num in arr:
            cur = max(cur + num, num)
            res = max(res, cur)
        return res % (10 ** 9 + 7)
