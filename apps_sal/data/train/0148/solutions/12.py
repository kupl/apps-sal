class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        worker.sort()

        m = len(worker)
        n = len(jobs)

        j = 0
        max_profit = 0
        result = 0
        for i in range(m):
            ability = worker[i]

            while j < n and jobs[j][0] <= ability:
                max_profit = max(max_profit, jobs[j][1])
                j += 1

            result += max_profit

        return result
