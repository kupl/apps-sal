class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # dp
        max_len = 1
        dp = {}
        for a in arr:
            if a - difference in dp:
                dp[a] = dp[a - difference] + 1
                max_len = max(max_len, dp[a])
            else:
                dp[a] = 1
        return max_len

        # # brute force
        # max_len = 1
        # for i in range(len(arr)):
        #     curr_tail = arr[i]
        #     curr_len = 1
        #     for j in range(i + 1, len(arr)):
        #         if arr[j] - curr_tail == difference:
        #             curr_len += 1
        #             curr_tail = arr[j]
        #     max_len = max(max_len, curr_len)
        # return max_len
