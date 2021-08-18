class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        q = [(headID, 0)]
        subordinates = collections.defaultdict(list)
        res = 0

        for i, v in enumerate(manager):
            subordinates[v].append(i)

        while q:
            u, time = q.pop(0)
            res = max(res, time)
            for v in subordinates[u]:
                q.append((v, time + informTime[u]))
        return res
