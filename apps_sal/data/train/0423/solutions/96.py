class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        if len(arr) == 1:
            return 1
        d = {arr[0]: 1}
        for i in range(1, len(arr)):
            if arr[i] - difference in d:
                d[arr[i]] = d[arr[i] - difference] + 1
            else:
                d[arr[i]] = 1
        return max(d.values())
