from heapq import *


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker.sort()
        difficulty_min_heap = []
        profit_max_heap = []

        total = 0

        for i in range(len(profit)):
            heappush(difficulty_min_heap, (difficulty[i], i))

        for w in worker:
            while difficulty_min_heap and difficulty_min_heap[0][0] <= w:
                current_difficulty, job_id = heappop(difficulty_min_heap)
                heappush(profit_max_heap, (-profit[job_id], job_id))
            if profit_max_heap:
                total += -profit_max_heap[0][0]

        return total
