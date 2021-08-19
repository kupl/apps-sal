import heapq
from collections import defaultdict, deque


class Solution(object):

    def numOfMinutes(self, n, headID, manager, informTime):
        if not manager or not informTime:
            return 0
        sub = defaultdict(list)
        q = [(0, headID)]
        heapq.heapify(q)
        used = {}
        for i in range(len(manager)):
            sub[manager[i]].append(i)
        while q:
            (spent, emp) = heapq.heappop(q)
            if used.get(emp, -1) != -1:
                continue
            used[emp] = spent
            for next_emp in sub[emp]:
                if used.get(next_emp, -1) == -1:
                    heapq.heappush(q, (spent + informTime[emp], next_emp))
        return max(used.values())
