class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # idea is similar to 300. Longest Increasing Subsequence
        # but instead of using a dp array and use nested for loop to
        # check condition, we can store the cur dp results in a hash map
        # so that we don't need a second for loop to check conditions.
        # dp = [1 for _ in range(len(arr))]
        # for i in range(len(dp)):
        #     for j in range(i):
        #         if arr[i]-arr[j] == difference:
        #             dp[i] = max(dp[i], 1+dp[j])
        # return max(dp)
        
        # stores the cur results of longest sequence
        dp = {}
        ans = 1
        for i in range(len(arr)):
            count = 1
            # update count for current if
            # condition is met
            if arr[i]-difference in dp:
                count += dp[arr[i]-difference]
            # store cur results
            dp[arr[i]] = count
            ans = max(ans, count)
        return ans
