from functools import lru_cache


class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:

        next_larger_idx = [None] * len(A)
        next_smaller_idx = [None] * len(A)

        sorted_idx_asc = sorted(list(range(len(A))), key=lambda i: A[i])
        sorted_idx_desc = sorted(list(range(len(A))), key=lambda i: A[i], reverse=True)

        stack = []
        for idx in sorted_idx_asc:
            while stack and stack[-1] < idx:
                prev_idx = stack.pop()
                next_larger_idx[prev_idx] = idx
            stack.append(idx)

        stack = []
        for idx in sorted_idx_desc:
            while stack and stack[-1] < idx:
                prev_idx = stack.pop()
                next_smaller_idx[prev_idx] = idx
            stack.append(idx)

        def get_next(idx, is_odd):
            if is_odd:
                return next_larger_idx[idx]
            else:
                return next_smaller_idx[idx]

        @lru_cache(maxsize=len(A) * 3)
        def is_goalable_from(idx, is_odd):
            if idx == len(A) - 1:
                return True
            if is_odd:
                smallest_idx = get_next(idx, is_odd)
                if smallest_idx is None:
                    return False
                return is_goalable_from(smallest_idx, not is_odd)
            else:
                largest_idx = get_next(idx, is_odd)
                if largest_idx is None:
                    return False
                return is_goalable_from(largest_idx, not is_odd)

        counts = 0
        for start_idx in range(len(A)):
            if is_goalable_from(start_idx, True):
                counts += 1
        return counts
