class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        d = collections.defaultdict(list)
        for init in initial:
            visit = set(initial)
            q = collections.deque([init])
            while q:
                node = q.popleft()
                for i in range(len(graph[node])):
                    if graph[node][i] == 0 or i in visit:
                        continue
                    visit.add(i)
                    d[i].append(init)
                    q.append(i)

        res = [0] * len(graph)
        for m in d:
            if len(d[m]) == 1:
                res[d[m][0]] += 1
        if max(res) == 0:
            return min(initial)
        return res.index(max(res))
