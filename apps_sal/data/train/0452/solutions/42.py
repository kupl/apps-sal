class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        res = [0]
        dp = {}

        def helper(i, d):
            if d == 0 and i == n:
                return 0
            if i >= n or d <= 0 or i + d > n:
                return float('inf')

            if (i, d) in dp:
                return dp[(i, d)]

            cur_max = 0
            cur_res = float('inf')
            for j in range(i, n):
                cur_max = max(cur_max, jobDifficulty[j])
                cur_res = min(cur_res, cur_max + helper(j + 1, d - 1))

            dp[(i, d)] = cur_res
            return cur_res

        res = helper(0, d)
        return res if res != float('inf') else -1
