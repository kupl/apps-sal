class Solution:

    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        index = 0
        count = len(graph)
        initial.sort()

        def search(removed):
            visited = set()
            dfs = []
            for i in initial:
                if i != removed:
                    dfs.append(i)
            while dfs:
                curr = dfs.pop()
                if curr in visited:
                    continue
                visited.add(curr)
                for (n, i) in enumerate(graph[curr]):
                    if n == removed:
                        continue
                    if i:
                        dfs.append(n)
            return len(visited)
        for i in initial:
            z = search(i)
            print(i, z)
            if z < count:
                index = i
                count = z
        return index
