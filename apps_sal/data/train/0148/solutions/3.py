from queue import PriorityQueue


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
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

        return profit
