class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        graph = defaultdict(list)
        for i, mgr in enumerate(manager):
            graph[mgr].append(i)

        q = deque()
        q.append((-1, 0))
        seen = set([-1])
        ans = 0

        while q:
            node, cumSum = q.popleft()
            ans = max(ans, cumSum)
            for sub in graph[node]:
                if sub not in seen:
                    seen.add(sub)
                    q.append((sub, cumSum + informTime[sub]))
        return ans
