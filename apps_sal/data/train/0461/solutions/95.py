class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = collections.defaultdict(list)
        for (i, c) in enumerate(manager):
            if c != -1:
                graph[c].append(i)
        que = [(headID, 0)]
        ans = 0
        while que:
            (node, time) = que.pop(0)
            ans = max(ans, time)
            for i in graph[node]:
                que.append((i, time + informTime[node]))
        return ans
