
import functools


class Solution:

    def minDifficulty(self, A, d):
        if len(A) < d:
            return -1

        @functools.lru_cache(None)
        def dfs(i, d):
            if d == 1:
                return max(A[i:])
            res = float('inf')
            max_cost_current_day = 0
            for j in range(i, len(A) - d + 1):
                # i'm percorring the array and trying all possibilites
                # the cost of a day is the max task on it
                max_cost_current_day = max(max_cost_current_day, A[j])
                # res = current_day_cost + others_days cost
                res = min(res, max_cost_current_day + dfs(j + 1, d - 1))
            return res
        return dfs(0, d)

