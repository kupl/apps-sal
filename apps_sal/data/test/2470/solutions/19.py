import bisect
from functools import lru_cache


class Solution:
    def makeArrayIncreasing(self, A: List[int], B: List[int]) -> int:
        B = sorted(set(B))
        b2idx = {b: i for i, b in enumerate(B)}
        
        @lru_cache(None)
        def find_larger_value_in_B(val):
            if val >= B[-1]:
                return float('inf')
            if val in b2idx:
                return B[b2idx[val] + 1]
            return B[bisect.bisect_right(B, val)]

        @lru_cache(None)
        def min_last_value_given_operations(n, ops):
            if ops < 0:
                return float('inf')
            elif n == 0:
                return float('-inf')
            elif ops > n:
                return min_last_value_given_operations(n, n)

            skip_op = min_last_value_given_operations(n - 1, ops)
            if skip_op == float('inf'):
                return float('inf')
            return min(
                A[n - 1] if skip_op < A[n - 1] else float('inf'),
                find_larger_value_in_B(min_last_value_given_operations(n - 1, ops - 1)),
            )

        last_success = -1
        for ops in range(min(len(A), len(B)), -1, -1):
            if min_last_value_given_operations(len(A), ops) == float('inf'):
                break
            last_success = ops

        return last_success

