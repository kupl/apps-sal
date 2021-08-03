# 6:12 -> 6:25 | 7:23 ->
# Find mapping of workers to jobs such that profit is maximized
# Greedy approach: take highest profit job, assign it to most highly skilled worker
from queue import PriorityQueue


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # print('difficulty', difficulty)
        # print('profit', profit)
        # print('worker', worker)
        pq = PriorityQueue()

        worker.sort()

        for i, job in enumerate(profit):
            pq.put((-job, i))

        profit = 0

        while worker:
            skill = worker.pop()
            cash, diff_index = pq.get() if not pq.empty() else (0, -1)
            while not pq.empty() and diff_index > -1 and skill < difficulty[diff_index]:
                cash, diff_index = pq.get()
            if skill < difficulty[diff_index]:
                cash, diff_index = 0, -1
            if cash != 0:
                pq.put((cash, diff_index))
            cash *= -1
            profit += cash
            # print(profit, cash, skill)

        return profit
