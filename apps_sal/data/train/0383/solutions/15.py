import collections


class Solution(object):
    def minMalwareSpread(self, graph, initial):
        N = len(graph)
        clean = set(range(N)) - set(initial)

        def dfs(u, seen):
            for v, adj in enumerate(graph[u]):
                if adj and v in clean and v not in seen:
                    seen.add(v)
                    dfs(v, seen)

        # For each node u in initial, dfs to find
        # 'seen': all nodes not in initial that it can reach.
        infected_by = {v: [] for v in clean}
        for u in initial:
            seen = set()
            dfs(u, seen)

            # For each node v that was seen, u infects v.
            for v in seen:
                infected_by[v].append(u)

        # For each node u in initial, for every v not in initial
        # that is uniquely infected by u, add 1 to the contribution for u.
        contribution = collections.Counter()
        for v, neighbors in infected_by.items():
            if len(neighbors) == 1:
                contribution[neighbors[0]] += 1

        # Take the best answer.
        best = (-1, min(initial))
        for u, score in contribution.items():
            if score > best[0] or score == best[0] and u < best[1]:
                best = score, u
        return best[1]
