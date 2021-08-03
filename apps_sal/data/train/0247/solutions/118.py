class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        LARGE_NUMBER = 1000000000

        if not arr:
            return -1

        psum = [0] * (len(arr) + 1)
        sum2i = {}

        for i in range(len(arr)):
            psum[i + 1] = psum[i] + arr[i]

        res = LARGE_NUMBER

        dp = [LARGE_NUMBER] * (len(arr) + 1)
        for i, x in enumerate(psum):
            assert x not in sum2i
            sum2i[x] = i
            if i > 0:
                dp[i] = dp[i - 1]

            if psum[i] - target in sum2i:
                j = sum2i[psum[i] - target]
                dp[i] = min(dp[i], i - j)
                if dp[j] != LARGE_NUMBER:
                    res = min(res, dp[j] + i - j)

        return res if res != LARGE_NUMBER else -1
