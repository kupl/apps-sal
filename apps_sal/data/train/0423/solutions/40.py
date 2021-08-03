class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        l = len(arr)
        index_map = {}
        for i in range(l):

            if (arr[i] - difference) in index_map:
                j = index_map[arr[i] - difference]
                dp[i] = dp.get(j, 1) + 1
            index_map[arr[i]] = i
        return max(dp.values()) if dp else 1
