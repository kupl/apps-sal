class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = collections.defaultdict(list)
        for i in range(len(manager)):
            if i == headID:
                continue
            graph[manager[i]].append(i)
        time = 0
        q = collections.deque([(headID, 0)])
        while q:
            node = q.popleft()
            time = max(time, node[1])
            for v in graph[node[0]]:
                q.append((v, node[1] + informTime[node[0]]))
        return time

