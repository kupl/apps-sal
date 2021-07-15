class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        n = len(graph)
        d = collections.defaultdict(list)
        for init in initial:
            vis = set(initial)
            Q = collections.deque([init])
            while Q:
                infect = Q.popleft()
                for node in range(len(graph[infect])):
                    if graph[infect][node] == 0:
                        continue
                    if node in vis:
                        continue
                    vis.add(node)
                    d[node].append(init)
                    Q.append(node)
        res = [0]*n
        for key in d:
            if len(d[key])==1:
                res[d[key][0]] += 1
        if max(res) == 0: return min(initial)
        return res.index(max(res))

