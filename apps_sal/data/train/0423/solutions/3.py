class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = [1 for a in arr]
        ele = collections.defaultdict(list)
        for i,x in enumerate(arr):
            ele[x].append(i)
        for i, a in enumerate(arr):
            if a - difference in ele:
                for j in ele[a-difference]:
                    if j<i:
                        dp[i] = max(dp[j] + 1,dp[i])
        return max(dp)
