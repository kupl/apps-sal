from functools import lru_cache


class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:

        N, S = len(A), sum(A)

        @lru_cache(None)
        def combinationSum(target, start, k):
            if target == 0:
                return k == 0
            if start == N or k < 0 or target < 0:
                return False

            return combinationSum(target - A[start], start + 1, k - 1) or combinationSum(target, start + 1, k)

        for k in range(1, N // 2 + 1):
            if S * k % N == 0:
                if combinationSum(S * k // N, 0, k):
                    return True

        return False
