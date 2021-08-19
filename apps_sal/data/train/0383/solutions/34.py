from collections import Counter, defaultdict


class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        # Total nodes
        N = len(graph)
        seen = set()
        refcounter = Counter()

        # clean nodes which are not infected
        clean_nodes = set(range(N)) - set(initial)
        maxval = 0

        def dfs(node, seen):
            for v, adj in enumerate(graph[node]):
                if adj and v not in seen and v in clean_nodes:
                    seen.add(node)
                    dfs(v, seen)

        for key in initial:
            seen = set()
            dfs(key, seen)
            refcounter[key] = len(seen)
            if maxval < refcounter[key]:
                maxval = refcounter[key]
            seen.clear()

        print(refcounter)

        maxlist = [key for key, val in list(refcounter.items()) if refcounter[key] == maxval]
        if not maxlist or len(maxlist) > 1:
            return sorted(initial)[0]
        return maxlist[0]
