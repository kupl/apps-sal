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
            
            # for k in list(dic.keys()):
            #     if k + difference == arr[i]:
            #         # print(k, difference, arr[i])
            #         dic[arr[i]] = dic[k] + [arr[i]]
            #         if arr[i] != k:
            #             dic.pop(k)
            #         temp = True
            #     elif k == arr[i]:
            #         temp = True
            if not temp:
                dic[arr[i]] = [arr[i]]
            # print(arr[i], dic)
        return max(list([len(x) for x in list(dic.values())]))

