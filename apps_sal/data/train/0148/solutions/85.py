from typing import List
import heapq


class Solution:

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        result_profit = 0
        profit_minus_min_heap = list()
        for i in range(len(profit)):
            heapq.heappush(profit_minus_min_heap, (-profit[i], difficulty[i]))
        worker_minus_min_heap = [-worker[i] for i in range(len(worker))]
        heapq.heapify(worker_minus_min_heap)
        while len(worker_minus_min_heap) != 0 and len(profit_minus_min_heap) != 0:
            (job_profit, job_difficulty) = profit_minus_min_heap[0]
            job_profit = -job_profit
            worker_ability = worker_minus_min_heap[0]
            worker_ability = -worker_ability
            if worker_ability >= job_difficulty:
                result_profit += job_profit
                heapq.heappop(worker_minus_min_heap)
            else:
                heapq.heappop(profit_minus_min_heap)
        return result_profit
