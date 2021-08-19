class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        dict_ = {}
        for num in arr:
            if num not in dict_:
                dict_[num] = 1
            else:
                dict_[num] += 1
        sort_list = sorted(dict_.keys(), key=lambda x: dict_[x], reverse=True)
        n = len(arr)
        size = 0
        for num in sort_list:
            n -= dict_[num]
            size += 1
            if n < len(arr) // 2 + 1:
                return size
