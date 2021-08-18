import bisect
from functools import lru_cache


class Solution:
    def makeArrayIncreasing(self, A: List[int], B: List[int]) -> int:
        B = sorted(set(B))

        def find_lower_val_in_B(val):
            larger_equal_idx = bisect.bisect_left(B, val)
            if larger_equal_idx > 0:
                return B[larger_equal_idx - 1]
            return None

        @lru_cache(None)
        def make_prefix_increasing(n, upper=float('inf')):
            if n == 0:
                return 0

            swap_b = find_lower_val_in_B(upper)
            ret = float('inf')
            if A[n - 1] < upper:
                ret = min(make_prefix_increasing(n - 1, upper=A[n - 1]), ret)
            if swap_b is not None:
                ret = min(1 + make_prefix_increasing(n - 1, upper=swap_b), ret)

            return ret

        ret = make_prefix_increasing(len(A))
        return ret if ret < float('inf') else -1
