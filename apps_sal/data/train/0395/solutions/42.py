from typing import List


class Solution:

    def build_next_greater_el_array(self, increasing_elements_idxs, next_bigger_el_idxs):
        decr_stack = []
        for idx in increasing_elements_idxs:
            while len(decr_stack) > 0 and decr_stack[-1] < idx:
                prev_idx = decr_stack.pop()
                next_bigger_el_idxs[prev_idx] = idx
            decr_stack.append(idx)

    def oddEvenJumps(self, arr: List[int]) -> int:
        if len(arr) == 0:
            return 0
        arr_with_idx = [[arr[i], i] for i in range(len(arr))]
        arr_with_idx_sorted = sorted(arr_with_idx, key=lambda x: x[0])
        increasing_elements_idxs = list(map(lambda x: x[1], arr_with_idx_sorted))
        next_bigger_el_idxs = [None for i in range(len(arr))]
        self.build_next_greater_el_array(increasing_elements_idxs, next_bigger_el_idxs)
        arr_with_idx_sorted_desc = sorted(arr_with_idx, key=lambda x: x[0], reverse=True)
        increasing_elements_idxs_desc = list(map(lambda x: x[1], arr_with_idx_sorted_desc))
        next_smaller_el_idxs = [None for i in range(len(arr))]
        self.build_next_greater_el_array(increasing_elements_idxs_desc, next_smaller_el_idxs)
        higher = [False for i in range(len(arr))]
        lower = [False for i in range(len(arr))]
        higher[-1] = True
        lower[-1] = True
        result = 1
        for i in range(len(arr) - 2, -1, -1):
            next_bigger_el_idx = next_bigger_el_idxs[i]
            next_smaller_el_idx = next_smaller_el_idxs[i]
            if next_bigger_el_idx is not None:
                lower[i] = higher[next_bigger_el_idx]
            if next_smaller_el_idx is not None:
                higher[i] = lower[next_smaller_el_idx]
            if lower[i] is True:
                result += 1
        return result
