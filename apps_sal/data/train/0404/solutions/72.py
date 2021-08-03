import functools


class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        @functools.lru_cache(None)
        def dp(start, p):
            if p == 1:
                return sum(A[start:]) / (len(A) - start)
            if start == len(A):
                return 0
            curr_sum = A[start]
            ret = 0
            for i in range(start + 1, len(A)):
                avg = curr_sum / (i - start)
                ret = max(ret, avg + dp(i, p - 1))
                curr_sum += A[i]
            return ret
        return dp(0, K)
