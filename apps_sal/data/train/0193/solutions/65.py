class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        arr_len = len(arr)
        int_dict = {}
        val = []
        for i in arr:
            int_dict[i] = int_dict.setdefault(i, 0) + 1
        for i in int_dict:
            val.append(int_dict[i])
        val.sort()
        count_num = 0
        loc = 0
        for i in val[::-1]:
            count_num += i
            loc += 1
            if count_num >= arr_len / 2:
                break
        return loc
