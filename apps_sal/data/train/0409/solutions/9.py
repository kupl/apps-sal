class Solution:

    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        n = len(arr)
        sums = sum(arr)
        dp = 0
        ans = -float('inf')
        for i in range(n * min(2, k)):
            cur = arr[i % n]
            dp = max(dp + cur, cur)
            ans = max(dp, ans)
        return max(0, ans, ans + sums * max(k - 2, 0)) % (10 ** 9 + 7)
