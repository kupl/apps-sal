from functools import lru_cache


class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:

        # mem = {}
        @lru_cache(None)
        def find(target, k, i):

            if k == 0:
                return target == 0

            if k + i > len(A):
                return False

            # if (target, k, i) in mem: return mem[(target, k, i)]

            ans = find(target - A[i], k - 1, i + 1) or find(target, k, i + 1)

            return ans

        n, s = len(A), sum(A)

        return any(find(s * j // n, j, 0) for j in range(1, n // 2 + 1) if s * j % n == 0)
