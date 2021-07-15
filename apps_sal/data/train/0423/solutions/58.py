import bisect
class Solution:
    def longestSubsequence(self, arr, diff):
        ''' DP solution O(N^2)

        dp = [1]*len(arr)
        l_sub_seq = 1
        for i in range(1, len(arr)):
            for j in range(i):
                if arr[i] - arr[j] == diff:
                    dp[i] = max(dp[i], dp[j] + 1)
                    l_sub_seq = max(dp[i], l_sub_seq)
        return l_sub_seq
        '''
        dp = {}
        ans = 0
        for i in arr:
            if i - diff in dp:
                dp[i] = dp[i - diff] + 1
            else:
                dp[i] = 1
            ans = max(ans, dp[i])
        return ans

