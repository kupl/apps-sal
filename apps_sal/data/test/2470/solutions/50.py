import bisect
from functools import lru_cache


class Solution:
    def makeArrayIncreasing(self, A: List[int], B: List[int]) -> int:
        B = sorted(set(B))

        def find_larger_value_in_B(val):
            if val >= B[-1]:
                return float('inf')
            return B[bisect.bisect_right(B, val)]

        @lru_cache(None)
        def min_last_value_given_operations(n, ops):
            if ops < 0:
                return float('inf')
            if n == 0:
                return float('-inf')

            ops = min(n, ops)
            return min(
                A[n - 1] if min_last_value_given_operations(n - 1, ops) < A[n - 1] else float('inf'),
                find_larger_value_in_B(min_last_value_given_operations(n - 1, ops - 1)),
            )

        for ops in range(min(len(A), len(B)) + 1):
            if min_last_value_given_operations(len(A), ops) < float('inf'):
                return ops

        return -1
