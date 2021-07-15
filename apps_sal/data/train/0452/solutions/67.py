class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        MAX = 300 * 1000 * 10
        N = len(jobDifficulty)
        cache = {}
        max_jobDifficulty = []
        for i in range(0, N):
            max_ij = [jobDifficulty[i]]
            for j in range(i+2, N+1):
                max_ij.append(max(max_ij[-1], jobDifficulty[j-1]))
            max_jobDifficulty.append(max_ij)
        def get_max_jobDifficulty(i, j):
            return max_jobDifficulty[i][j-i-1]
        def dp(left_days: int, left_jobs_i: int, current_jobs_i: int) -> int:
            key = (left_days, left_jobs_i, current_jobs_i)
            if key not in cache:
                n_left_jobs = N - left_jobs_i
                if n_left_jobs == 0:
                    assert left_days > 0
                    if left_days == 1 and current_jobs_i < left_jobs_i:
                        cost = get_max_jobDifficulty(current_jobs_i, left_jobs_i)
                    else:
                        cost = MAX
                elif n_left_jobs == left_days:
                    cost = get_max_jobDifficulty(current_jobs_i, left_jobs_i + 1) + sum(jobDifficulty[(left_jobs_i + 1):])
                else:
                    cost = dp(left_days, left_jobs_i + 1, current_jobs_i)
                    if left_days > 1:
                        cost = min(cost, dp(left_days - 1, left_jobs_i + 1, left_jobs_i + 1) + get_max_jobDifficulty(current_jobs_i, left_jobs_i + 1))
                cache[key] = cost
            return cache[key]
        ret = dp(d, 0, 0)
        if ret >= MAX:
            return -1
        return ret
