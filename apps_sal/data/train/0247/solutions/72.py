class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        if not arr:
            return -1

        def getdp(arr):
            dp = [float('inf')] * (len(arr))
            summ = 0
            lookup = defaultdict(int)
            for index, num in enumerate(arr):
                summ += num
                if summ == target:
                    dp[index] = index - 0 + 1
                elif summ - target in lookup:
                    dp[index] = min(index - lookup[summ - target] + 1, dp[index - 1])
                else:
                    dp[index] = dp[index - 1]

                lookup[summ] = index + 1
            return dp

        dp_left = getdp(arr)
        dp_right = getdp(arr[::-1])[::-1]

        ans = float('inf')
        for i in range(1, len(arr)):
            ans = min(ans, dp_left[i - 1] + dp_right[i])
        return ans if (ans != float('inf')) else -1
