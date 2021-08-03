def maximum_profit_for_difficulty(diff_job, difficulty, profit):
    return max([profit[job] for job in diff_job[difficulty]])


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        min_difficulty = min(difficulty)
        max_difficulty = max(difficulty)
        diff_job = defaultdict(list)
        for i, diff in enumerate(difficulty):
            diff_job[diff].append(i)

        max_profit = [maximum_profit_for_difficulty(diff_job, min_difficulty, profit)]
        for i in range(1, max_difficulty - min_difficulty + 1):
            current_difficulty = i + min_difficulty
            if current_difficulty in diff_job:
                current_job_profit = maximum_profit_for_difficulty(diff_job, current_difficulty, profit)
                max_profit.append(max(max_profit[i - 1], current_job_profit))
            else:
                max_profit.append(max_profit[i - 1])

        result = 0
        for ability in worker:
            if ability >= max_difficulty:
                result += max_profit[-1]
            elif ability < min_difficulty:
                result += 0
            else:
                result += max_profit[ability - min_difficulty]
        return result
