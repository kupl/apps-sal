import collections


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        d = collections.defaultdict(list)
        for i, k in enumerate(manager):
            if i == headID:
                continue

            d[k].append(i)

        q = [(0, headID)]
        total = 0
        while q:
            time, node = q.pop(0)
            for i in d[node]:
                q.append((time + informTime[node], i))
                total = max(total, time + informTime[node])
        return total
