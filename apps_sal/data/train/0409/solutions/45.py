from itertools import accumulate


class Solution:

    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        if not arr:
            return 0
        MOD = 10 ** 9 + 7

        def kadane(arr):
            return max(accumulate(arr, func=lambda a, b: a + b if a > 0 else b, initial=0))
        return ((k - 2) * max(sum(arr), 0) + kadane(arr * 2)) % MOD if k >= 2 else kadane(arr)
