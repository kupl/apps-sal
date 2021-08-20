class Solution:

    def dfs(self, graph, s, des, steps, visited):
        if self.res != -1 and steps >= self.res:
            return
        if s in des:
            if self.res == -1:
                self.res = steps
            else:
                self.res = min(self.res, steps)
            return
        if s not in graph:
            return
        for i in graph[s]:
            if i not in visited:
                visited.add(i)
                self.dfs(graph, i, des, steps + 1, visited)
                visited.remove(i)

    def numBusesToDestination(self, routes: List[List[int]], s: int, t: int) -> int:
        if s == t:
            return 0
        des = set()
        starts = set()
        stop_to_bus = {}
        graph = {}
        for bus in range(0, len(routes)):
            for stop in routes[bus]:
                if stop == s:
                    starts.add(bus)
                if stop == t:
                    des.add(bus)
                if stop not in stop_to_bus:
                    stop_to_bus[stop] = set()
                stop_to_bus[stop].add(bus)
        for (_, v) in list(stop_to_bus.items()):
            for i in v:
                for j in v:
                    if i == j:
                        continue
                    if i not in graph:
                        graph[i] = set()
                    graph[i].add(j)
        self.res = -1
        visited = set()
        for s in starts:
            visited.add(s)
            self.dfs(graph, s, des, 1, visited)
            visited.remove(s)
        return self.res
