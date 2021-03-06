class Solution:

    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        n = len(arr1)

        def get_max(arr):
            max_val = 0
            (min_val, min_idx) = (float('inf'), float('inf'))
            for (idx, val) in enumerate(arr):
                if min_idx < float('inf'):
                    abs_max = val - min_val + idx - min_idx
                    if abs_max > max_val:
                        max_val = abs_max
                if val + idx < min_val + min_idx:
                    (min_val, min_idx) = (val, idx)
            return max_val
        max_abs = 0
        for first in [-1, 1]:
            for second in [-1, 1]:
                arr = []
                for i in range(n):
                    arr.append(first * arr1[i] + second * arr2[i])
                max_abs = max(get_max(arr), max_abs)
        return max_abs
