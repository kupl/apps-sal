class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dic = {}
        for i in range(len(arr)):
            if (arr[i] - difference) in dic:
                dic[arr[i]] = dic[arr[i] - difference] + 1
            else:
                dic[arr[i]] = 1
        return max(dic.values())
