class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:

        job = {}
        for cost, gain in zip(difficulty, profit):
            if cost in job:
                job[cost] = max(job[cost], gain)
            else:
                job[cost] = gain

        job = [(k, v) for k, v in list(job.items())] + [(0, 0)]
        job.sort()
        useless = set()

        global_max = -float('inf')
        for i, (c, g) in enumerate(job):
            if g < global_max:
                useless.add(i)
            else:
                global_max = g

        job = [job[i] for i in range(len(job)) if i not in useless]
        print(job)
        worker.sort()

        i, j = 0, 0
        ans = 0
        while j < len(worker):

            while job[i][0] < worker[j] and i < len(job) - 1:
                i += 1

            ans += job[i][1] if job[i][0] <= worker[j] else job[i - 1][1]

            j += 1

        return ans
