class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        groups = dict()
        sorted_original_idx_and_days = sorted(enumerate(bloomDay), key=lambda item: item[1])

        SIZE = len(sorted_original_idx_and_days)
        bloom_flag = [False] * SIZE
        max_right = [-1] * SIZE
        min_left = [-1] * SIZE
        count = 0

        merge_right_flag = False
        merge_left_flag = False
        for idx, (ith_flower, day) in enumerate(sorted_original_idx_and_days):
            bloom_flag[ith_flower] = True
            max_right[ith_flower] = min_left[ith_flower] = ith_flower
            merge_left_flag = merge_right_flag = False
            if ith_flower < SIZE - 1 and bloom_flag[ith_flower + 1]:
                merge_right_flag = True
                ptr = ith_flower + 1
                while max_right[ptr] != -1 and max_right[ptr] != ptr:
                    ptr = max_right[ptr]
                max_right[ith_flower] = ptr
            if ith_flower > 0 and bloom_flag[ith_flower - 1]:
                merge_left_flag = True
                ptr = ith_flower - 1
                while min_left[ptr] != -1 and min_left[ptr] != ptr:
                    ptr = min_left[ptr]
                min_left[ith_flower] = ptr
            max_right[min_left[ith_flower]] = max_right[ith_flower]
            min_left[max_right[ith_flower]] = min_left[ith_flower]

            if merge_left_flag:
                count -= (ith_flower - min_left[ith_flower]) // k
            if merge_right_flag:
                count -= (max_right[ith_flower] - ith_flower) // k
            count += ((max_right[ith_flower] + 1) - min_left[ith_flower]) // k

            if count >= m:
                return day
        return -1
