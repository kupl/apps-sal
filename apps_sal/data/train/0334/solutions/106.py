class Solution:

    def minCost(self, s: str, cost: List[int]) -> int:
        prev = None
        min_cost = 0
        pq = []
        for (char, c) in zip(s, cost):
            if not prev:
                prev = char
                heapq.heappush(pq, c)
            elif prev != char:
                prev = char
                while len(pq) > 1:
                    min_cost += heapq.heappop(pq)
                pq = [c]
            else:
                heapq.heappush(pq, c)
        while len(pq) > 1:
            min_cost += heapq.heappop(pq)
        return min_cost
