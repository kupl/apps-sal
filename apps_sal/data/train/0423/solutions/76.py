class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        if len(arr) == 1:
            return 1
        res, length = 1, len(arr)
        dp = {}
        dp[arr[-1]] = 1
        flag = 1

        for i in range(length - 2, -1, -1):
            if arr[i] not in dp:
                dp[arr[i]] = 1
                flag = 0
            if arr[i] + difference in dp:
                if difference == 0 and flag == 0:
                    flag = 1
                    continue
                dp[arr[i]] = max(dp[arr[i]], dp[arr[i] + difference] + 1, )
            res = max(res, dp[arr[i]])

        return res
