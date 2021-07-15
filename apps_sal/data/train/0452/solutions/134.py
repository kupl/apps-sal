class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        MAX = 300 * 1000 * 10
        N = len(jobDifficulty)
        cache = {}
        def dp(left_days: int, left_jobs_i: int, current_jobs_i: int) -> int:
            key = (left_days, left_jobs_i, current_jobs_i)
            if key not in cache:
                if left_jobs_i == N:
                    assert left_days > 0
                    if left_days == 1 and current_jobs_i < left_jobs_i:
                        cost = max(jobDifficulty[current_jobs_i:left_jobs_i])
                    else:
                        cost = MAX
                else:
                    cost = dp(left_days, left_jobs_i + 1, current_jobs_i)
                    if left_days > 1:
                        cost = min(cost, dp(left_days - 1, left_jobs_i + 1, left_jobs_i + 1) + max(jobDifficulty[current_jobs_i:(left_jobs_i + 1)]))
                cache[key] = cost
            return cache[key]
        ret = dp(d, 0, 0)
        if ret >= MAX:
            return -1
        return ret
