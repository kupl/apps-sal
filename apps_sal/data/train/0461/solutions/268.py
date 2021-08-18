import heapq


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        hierachy = {}
        for idx, m in enumerate(manager):
            if m not in hierachy:
                hierachy[m] = []
            hierachy[m].append(idx)

        time_needed = [-1] * n
        time_needed[headID] = 0

        q = [(0, headID)]

        while q:
            cost, node = heapq.heappop(q)
            time_needed[node] = cost
            for nei in hierachy.get(node, []):
                heapq.heappush(q, (time_needed[node] + informTime[node], nei))

        return max(time_needed)
