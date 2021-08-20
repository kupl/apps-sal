class Solution:

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = [0 for _ in range(len(arr))]
        lookup = {}
        for i in range(len(arr)):
            if arr[i] not in lookup:
                lookup[arr[i]] = [i]
            else:
                lookup[arr[i]].append(i)
        for i in range(len(arr) - 1, 0, -1):
            if arr[i] - difference in lookup:
                dp[i] = max(1, dp[i])
                for index in lookup[arr[i] - difference]:
                    if index < i:
                        dp[index] = dp[i] + 1
        return max(dp) if max(dp) > 0 else 1
