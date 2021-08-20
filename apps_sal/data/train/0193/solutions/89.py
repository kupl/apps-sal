from collections import defaultdict


class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        count_map = defaultdict(int)
        for num in arr:
            count_map[num] += 1
        res_arr = []
        for (num, count) in count_map.items():
            res_arr.append((count, num))
        res_arr = sorted(res_arr)[::-1]
        count = 0
        index = 0
        while count < len(arr) // 2:
            count += res_arr[index][0]
            index += 1
        return index
