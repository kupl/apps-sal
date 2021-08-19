from collections import Counter


class Solution:

    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        N = len(graph)
        clean = set(range(N)) - set(initial)

        def dfs(u, seen):
            for (v, adj) in enumerate(graph[u]):
                if adj and v in clean and (v not in seen):
                    seen.add(v)
                    dfs(v, seen)
        infected_by = {v: [] for v in clean}
        for u in initial:
            seen = set()
            dfs(u, seen)
            for v in seen:
                infected_by[v].append(u)
        contribution = Counter()
        for (v, neighbors) in list(infected_by.items()):
            if len(neighbors) == 1:
                contribution[neighbors[0]] += 1
        best = (-1, min(initial))
        for (u, score) in list(contribution.items()):
            if score > best[0] or (score == best[0] and u < best[1]):
                best = (score, u)
        return best[1]
