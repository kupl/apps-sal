class Solution:

    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        spreads = [[] for _ in range(len(graph))]
        initial = set(initial)
        for i in initial:
            q = {i}
            visited = set()
            while q:
                cur = q.pop()
                if cur in visited or (cur in initial and cur != i):
                    continue
                visited.add(cur)
                spreads[cur].append(i)
                for j in range(len(graph[cur])):
                    if graph[cur][j]:
                        q.add(j)
        counts = defaultdict(int)
        for s in spreads:
            if len(s) == 1:
                counts[s[0]] += 1
        most = next(iter(initial))
        for (i, c) in list(counts.items()):
            if c > counts[most] or (c == counts[most] and i < most):
                most = i
        return most
