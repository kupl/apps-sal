import collections


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = collections.defaultdict(list)
        for i in range(len(manager)):
            if manager[i] != -1:
                graph[manager[i]].append(i)
        queue = [(headID, 0)]
        ans = 0
        while queue:
            temp = []
            maxx = 0
            for m, val in queue:
                ans = max(ans, val)
                for w in graph[m]:
                    temp.append((w, val + informTime[m]))
            queue = temp
        return ans
