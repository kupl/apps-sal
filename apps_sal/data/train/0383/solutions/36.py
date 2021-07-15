class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        def infected(src, exclude=None):
            infected = set()
            def dfs(node, infected):
                if node in infected:
                    return
                infected |= {node}
                for neighbor in range(len(graph[node])):
                    if graph[node][neighbor]==0 or neighbor==exclude:
                        continue
                    dfs(neighbor, infected)
            for source in src:
                if source == exclude:
                    continue
                dfs(source, infected)
            return len(infected)
        initial.sort()
        res, best = initial[0], len(graph)
        for source in initial:
            temp = infected(initial, source)
            if temp < best:
                res, best = source, temp
        return res
