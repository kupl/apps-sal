class Solution:

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        num2len = dict()
        res = 0
        for i in range(len(arr)):
            if arr[i] - difference in num2len:
                num2len[arr[i]] = num2len[arr[i] - difference] + 1
            else:
                num2len[arr[i]] = 1
            res = max(res, num2len[arr[i]])
        return res
