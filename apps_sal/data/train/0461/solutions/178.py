class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for (child, parent) in enumerate(manager):
            graph[parent].append(child)
        q = deque([(headID, informTime[headID])])
        maxval = 0
        while q:
            (head, time) = q.popleft()
            maxval = max(maxval, time)
            for child in graph[head]:
                q.append((child, time + informTime[child]))
        return maxval
