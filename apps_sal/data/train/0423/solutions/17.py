class Solution:

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dic = {}
        for i in range(len(arr)):
            temp = False
            if arr[i] - difference in list(dic.keys()):
                dic[arr[i]] = dic[arr[i] - difference] + [arr[i]]
                if arr[i] != arr[i] - difference:
                    dic.pop(arr[i] - difference)
                temp = True
            elif arr[i] in list(dic.keys()):
                temp = True
            if not temp:
                dic[arr[i]] = [arr[i]]
        return max(list([len(x) for x in list(dic.values())]))
