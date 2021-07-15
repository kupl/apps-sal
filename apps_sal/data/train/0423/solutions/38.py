class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        if len(arr) == 1:
            return 1
        dp = [1] * len(arr)
        dic = {arr[0]:0}
        for i in range(1, len(dp)):
            dic[arr[i]] = i
            if arr[i] - difference in dic:
                dp[i] = max(dp[i], dp[dic[arr[i]-difference]]+1)
        return max(dp)
