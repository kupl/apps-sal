class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        group_size = [0 for _ in range(len(arr) + 1)]
        parent_idx = [-1 for _ in range(len(arr) + 1)]
        res = -1
        num_same = 0
        for i in range(1, len(arr) + 1):
            num = arr[i - 1]
            this_group = 1
            group_start = num
            group_end = num
            if num > 0 and group_size[num - 1] > 0:
                this_group += group_size[num - 1]
                group_start = parent_idx[num - 1]
                if group_size[num - 1] == m:
                    num_same -= 1
            if num < len(arr) and group_size[num + 1] > 0:
                this_group += group_size[num + 1]
                group_end = num + group_size[num + 1]
                if group_size[num + 1] == m:
                    num_same -= 1
            group_size[num] = this_group
            group_size[group_start] = this_group
            group_size[group_end] = this_group
            parent_idx[num] = group_start
            parent_idx[group_end] = group_start
            if this_group == m:
                res = i
                num_same += 1
            elif num_same > 0:
                res = i
        return res
