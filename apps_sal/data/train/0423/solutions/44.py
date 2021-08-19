class Solution:

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        if not arr:
            return 0
        max_len = 0
        dp = [0] * len(arr)
        prev_max_len = {}
        for (i, num) in enumerate(arr):
            if (key := (arr[i] - difference)) in prev_max_len:
                dp[i] = prev_max_len[key] + 1
            else:
                dp[i] = 1
            prev_max_len[arr[i]] = dp[i]
            max_len = max(max_len, dp[i])
        return max_len
