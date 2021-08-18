class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker.sort()
        difprof = [(difficulty[i], profit[i]) for i in range(len(difficulty))]
        difprof.sort()
        total = 0

        index = 0
        maxProfit = 0
        for w in worker:
            while index < len(difprof) and w >= difprof[index][0]:
                maxProfit = max(maxProfit, difprof[index][1])
                index += 1

            total += maxProfit
        return total
