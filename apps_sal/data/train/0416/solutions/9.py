class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        N = len(graph)

        def parent(m, c, t):
            if t == 2:
                for m2 in graph[m]:
                    yield m2, c, 1
            else:
                for c2 in graph[c]:
                    if c2:
                        yield m, c2, 2
        D, M, C = 0, 1, 2
        color = collections.defaultdict(int)
        degree = {}
        for m in range(N):
            for c in range(N):
                degree[m, c, 1] = len(graph[m])
                degree[m, c, 2] = len(graph[c]) - (0 in graph[c])

        queue = collections.deque([])
        for i in range(N):
            for t in [1, 2]:
                color[0, i, t] = M
                queue.append((0, i, t, M))
                if i > 0:
                    color[i, i, t] = C
                    queue.append((i, i, t, C))

        while queue:
            i, j, t, w = queue.popleft()
            for i2, j2, t2 in parent(i, j, t):
                if color[i2, j2, t2] is D:
                    if t2 == w:
                        color[i2, j2, t2] = w
                        queue.append((i2, j2, t2, w))
                    else:
                        degree[i2, j2, t2] -= 1
                        if degree[i2, j2, t2] == 0:
                            color[i2, j2, t2] = 3 - t2
                            queue.append((i2, j2, t2, 3 - t2))

        return color[1, 2, 1]
