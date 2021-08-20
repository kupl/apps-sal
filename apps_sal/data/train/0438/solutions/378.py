from collections import defaultdict


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        size_records = defaultdict(int)
        range_records = defaultdict(list)
        ans = -1
        for (index, i) in enumerate(arr):
            new_range = [i, i]
            if range_records[i - 1]:
                new_range = [range_records[i - 1][0], i]
                size_records[range_records[i - 1][1] - range_records[i - 1][0] + 1] -= 1
            if range_records[i + 1]:
                new_range = [new_range[0], range_records[i + 1][1]]
                size_records[range_records[i + 1][1] - range_records[i + 1][0] + 1] -= 1
            size_records[new_range[1] - new_range[0] + 1] += 1
            range_records[new_range[0]] = new_range
            range_records[new_range[1]] = new_range
            if size_records[m]:
                ans = index + 1
        return ans
