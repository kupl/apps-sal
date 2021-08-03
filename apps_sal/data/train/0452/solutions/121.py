class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if d > len(jobDifficulty):
            return - 1

        last_day_max_efforts = [[float('inf')] * len(jobDifficulty) for _ in range(d)]

        last_day_max_efforts[0][0] = jobDifficulty[0]
        for i in range(1, len(jobDifficulty)):
            last_day_max_efforts[0][i] = max(last_day_max_efforts[0][i - 1], jobDifficulty[i])

        for day in range(1, d):
            for current_split in range(day, len(jobDifficulty)):
                for last_split in range(current_split):
                    last_day_max_efforts[day][current_split] = min(last_day_max_efforts[day][current_split], last_day_max_efforts[day - 1][last_split] + max(jobDifficulty[last_split + 1:current_split + 1]))

        return last_day_max_efforts[d - 1][len(jobDifficulty) - 1]
