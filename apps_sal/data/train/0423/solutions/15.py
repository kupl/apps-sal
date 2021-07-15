class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp, res = [0  for _  in range(len(arr))], 1
        lookup = {}
        for i in range(len(arr)):
            if arr[i] not in lookup:
                lookup[arr[i]] = [i]
            else:
                lookup[arr[i]].append(i)
        for i in range(len(arr)-1, 0, -1):
            diff = arr[i] - difference
            if  diff in lookup:
                dp[i] = max(1, dp[i])
                for index in lookup[diff]:
                    if index < i:
                        dp[index] = dp[i] + 1
                        res = max(res, dp[index])
        return res
