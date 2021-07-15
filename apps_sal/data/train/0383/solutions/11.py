class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        conn = collections.defaultdict(set)
        n = len(graph)
        visited = [False] * n
        for i in initial:
            visited[i] = True
            
        def bfs(node):
            q = collections.deque([node])
            v = visited[:]
            while q:
                i = q.popleft()
                for j, k in enumerate(graph[i]):
                    if k and not v[j]:
                        v[j] = True
                        q.append(j)
                        conn[j].add(node)
        for i in initial:
            bfs(i)
        cnt = collections.Counter()
        for k, v in list(conn.items()):
            if len(v) == 1:
                cnt[v.pop()] += 1
        if not cnt:
            return min(initial)
        s = sorted(list(cnt.items()), key=lambda k: (k[1], -k[0]))
        return s[-1][0]

