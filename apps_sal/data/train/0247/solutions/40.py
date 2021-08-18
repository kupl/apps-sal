from typing import List
import math
import sys


class Solution:
    def __init__(self):
        self.preceeding_soln_lens = []

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        self.preceeding_soln_lens = [sys.maxsize] * len(arr)
        min_len_sum = sys.maxsize
        buffer = []
        buffer_sum = 0
        buffer_len = 0

        i = 0
        while i < len(arr):
            buffer_sum += arr[i]
            buffer_len += 1
            buffer.append(i)

            sub_array_end_idx = buffer[-1]

            if buffer_sum < target:
                self.preceeding_soln_lens[sub_array_end_idx] = self.preceeding_soln_lens[sub_array_end_idx - 1]

            while buffer_sum >= target:
                popped_idx = buffer.pop(0)

                if buffer_sum == target:
                    self.preceeding_soln_lens[sub_array_end_idx] = min(buffer_len, self.preceeding_soln_lens[sub_array_end_idx - 1])

                    if popped_idx > 0:
                        non_overlapping_previous_soln_idx = popped_idx - 1
                        min_len_sum = min(min_len_sum, self.preceeding_soln_lens[non_overlapping_previous_soln_idx] + buffer_len)
                else:
                    self.preceeding_soln_lens[sub_array_end_idx] = self.preceeding_soln_lens[sub_array_end_idx - 1]

                buffer_len -= 1
                buffer_sum -= arr[popped_idx]

            i += 1

        if min_len_sum == sys.maxsize:
            return -1
        return min_len_sum
