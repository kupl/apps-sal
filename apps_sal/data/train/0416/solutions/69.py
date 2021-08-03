class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        mouse, cat = 1, 2
        node = defaultdict(int)
        graphLen = len(graph)
        # key = (m0, c0, t)
        stack = deque([])
        for l in graph[0]:
            for ci in range(1, graphLen):
                if ci != l:
                    node[(l, ci, mouse)] = mouse
                    stack.append((l, ci, mouse, mouse))
        for i in range(1, graphLen):
            for j in graph[i]:
                if j != 0:
                    node[(i, j, cat)] = cat
                    stack.append((i, j, cat, cat))
            node[(i, i, cat)] = cat
            node[(i, i, mouse)] = cat
            stack.append((i, i, cat, cat))
            stack.append((i, i, mouse, cat))

        degree = {}
        for i in range(graphLen):
            for j in range(graphLen):
                if i != j:
                    if (i, j, mouse) not in stack:
                        degree[(i, j, mouse)] = len(graph[i])
                    if (i, j, cat) not in stack:
                        degree[(i, j, cat)] = len(graph[j]) - (1 if 0 in graph[j] else 0)

        while stack:
            m0, c0, t0, w = stack.popleft()
            if t0 == mouse:
                if w == cat:
                    for move in graph[c0]:
                        if move != 0 and (m0, move, cat) not in node:
                            node[(m0, move, cat)] = cat
                            stack.append((m0, move, cat, cat))
                else:
                    for move in graph[c0]:
                        if move != 0 and (m0, move, cat) not in node:
                            degree[(m0, move, cat)] -= 1
                            if degree[(m0, move, cat)] == 0:
                                node[(m0, move, cat)] = mouse
                                stack.append((m0, move, cat, mouse))
            else:
                if w == mouse:
                    for move in graph[m0]:
                        if (move, c0, mouse) not in node:
                            node[(move, c0, mouse)] = mouse
                            stack.append((move, c0, mouse, mouse))
                else:
                    for move in graph[m0]:
                        if (move, c0, mouse) not in node:
                            degree[(move, c0, mouse)] -= 1
                            if degree[(move, c0, mouse)] == 0:
                                node[(move, c0, mouse)] = cat
                                stack.append((move, c0, mouse, cat))
        # print(node)
        return node[(1, 2, mouse)]
