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
            m, val = queue.pop(0)
            ans = max(ans, val)
            for w in graph[m]:
                queue.append((w, val+informTime[m]))
        return ans
                        

