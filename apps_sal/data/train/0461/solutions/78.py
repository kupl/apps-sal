class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        q = [(headID, 0)]

        graph = collections.defaultdict(list)
        for i in range(n):
            if manager[i] != -1:
                graph[manager[i]].append(i)

        res = 0

        while q:
            sz = len(q)
            for _ in range(sz):
                i, t = q.pop(0)
                t += informTime[i]
                res = max(res, t)
                for j in graph[i]:
                    q.append((j, t))

        return res
