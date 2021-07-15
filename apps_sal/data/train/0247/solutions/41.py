from typing import List
import heapq
import math
import sys


class Solution:
    def __init__(self):
        self.preceeding_soln_lens = []
        self.segment_tree = []

    def has_overlap(self, rng, list_of_ranges):
        s, e = rng
        if len(list_of_ranges):
            os, oe = list_of_ranges[-1]
            if e < os or oe < s:
                pass
            else:
                return True

        return False

    def find_min(self, s, e):
        min_val = sys.maxsize
        for i in range(s, e):
            if self.preceeding_soln_lens[i]:
                min_val = min(min_val, self.preceeding_soln_lens[i])
        if min_val == sys.maxsize:
            return None
        return min_val

    def n2_find(self, i, lengths):
        len_one = self.find_min(0,i)
        if len_one:
            len_two = self.find_min(i + len_one - 1, len(self.preceeding_soln_lens))
            if len_two:
                heapq.heappush(lengths, len_one+len_two)

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        # What's the best I can do ENDING at this index.
        self.preceeding_soln_lens = [sys.maxsize] * len(arr)
        min_len_sum = sys.maxsize
        buffer = []
        buffer_sum = 0
        buffer_len = 0

        i = 0
        # O(N)
        while i < len(arr):
            # update state
            buffer_sum += arr[i]
            buffer_len += 1
            buffer.append(i)

            sub_array_end_idx = buffer[-1]

            # check constraint
            if buffer_sum < target:
                # copy over the previous one
                self.preceeding_soln_lens[sub_array_end_idx] = self.preceeding_soln_lens[sub_array_end_idx-1]

            while buffer_sum >= target:
                popped_idx = buffer.pop(0)

                if buffer_sum == target:
                    # check for the min
                    self.preceeding_soln_lens[sub_array_end_idx] = min(buffer_len, self.preceeding_soln_lens[sub_array_end_idx-1])

                    if popped_idx > 0:
                        non_overlapping_previous_soln_idx = popped_idx - 1
                        min_len_sum = min(min_len_sum, self.preceeding_soln_lens[non_overlapping_previous_soln_idx] + buffer_len)
                else:
                    self.preceeding_soln_lens[sub_array_end_idx] = self.preceeding_soln_lens[sub_array_end_idx-1]

                buffer_len -= 1
                buffer_sum -= arr[popped_idx]

            i += 1

        if min_len_sum == sys.maxsize:
            return -1
        return min_len_sum
