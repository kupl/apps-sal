from collections import defaultdict


class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        if not graph:
            return -1
        n = len(graph)

        initial = sorted(initial)

        clean = set([i for i in range(n)]) - set(initial)
        infected_by = {i: [] for i in range(n)}

        def dfs(node):
            for i, v in enumerate(graph[node]):
                if v and i in clean and i not in seen:
                    seen.add(i)
                    dfs(i)
        for node in initial:
            seen = set()
            dfs(node)
            for u in seen:
                infected_by[u].append(node)

        cnt = {v: 0 for v in initial}

        for i in infected_by:
            if len(infected_by[i]) == 1:
                cnt[infected_by[i][0]] += 1
        m = 0
        res = initial[0]
        for i in cnt:
            if cnt[i] > m:
                res = i
                m = cnt[i]
        return res
