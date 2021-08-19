class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # dp[i] longest subsequece at i
        dic = {}
        ans = 1
        for x in arr:
            pre = x - difference
            dic[x] = dic.get(pre, 0) + 1
            ans = max(ans, dic[x])
        return max(dic.values())
