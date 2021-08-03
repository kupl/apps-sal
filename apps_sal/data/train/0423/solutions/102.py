class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        from collections import defaultdict
        indexMap = defaultdict(list)
        for i in range(len(arr) - 1, -1, -1):
            indexMap[arr[i]].append(i)

        dp = [1] * (len(arr))
        maxLen = 1
        for i in range(len(arr)):
            indexMap[arr[i]].pop()
            nextVal = arr[i] + difference
            if nextVal in indexMap and indexMap[nextVal]:
                j = indexMap[nextVal][-1]
                dp[j] = max(dp[i] + 1, dp[j])
                maxLen = max(maxLen, dp[j])
        return maxLen
