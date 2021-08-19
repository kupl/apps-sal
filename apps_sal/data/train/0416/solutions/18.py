class Solution:

    def catMouseGame(self, graph: List[List[int]]) -> int:
        memo = {}

        def mouse_play(key, cat, mouse, turn):
            if any((v == 0 for v in graph[mouse])):
                memo[key] = 1
                return 1
            res = 2
            for nxt in graph[mouse]:
                if nxt == cat:
                    continue
                tmp = move(cat, nxt, False)
                if tmp == 1:
                    res = 1
                    break
                if tmp == 0:
                    res = 0
            memo[key] = res
            return res

        def cat_play(key, cat, mouse, turn):
            if any((v == mouse for v in graph[cat])):
                memo[key] = 2
                return 2
            res = 1
            for nxt in graph[cat]:
                if nxt == 0:
                    continue
                tmp = move(nxt, mouse, True)
                if tmp == 2:
                    res = 2
                    break
                if tmp == 0:
                    res = 0
            memo[key] = res
            return res

        def move(cat, mouse, turn):
            key = (cat, mouse, turn)
            if key in memo:
                return memo[key]
            memo[key] = 0
            if turn:
                return mouse_play(key, cat, mouse, turn)
            else:
                return cat_play(key, cat, mouse, turn)
        return move(2, 1, True)

    def catMouseGame(self, graph: List[List[int]]) -> int:
        N = len(graph)
        (DRAW, MOUSE, CAT) = (0, 1, 2)

        def parents(m, c, t):
            if t == MOUSE:
                for c2 in graph[c]:
                    if c2:
                        yield (m, c2, 3 - t)
            if t == CAT:
                for m2 in graph[m]:
                    yield (m2, c, 3 - t)
        (color, degree) = (collections.defaultdict(int), {})
        for m in range(N):
            for c in range(N):
                degree[m, c, MOUSE] = len(graph[m])
                degree[m, c, CAT] = len(graph[c]) - (0 in graph[c])
        que = collections.deque()
        for i in range(N):
            for t in range(1, 3):
                color[0, i, t] = MOUSE
                que.append((0, i, t))
                if i > 0:
                    color[i, i, t] = CAT
                    que.append((i, i, t))
        while que:
            (m, c, t) = que.pop()
            col = color[m, c, t]
            for (m2, c2, t2) in parents(m, c, t):
                if color[m2, c2, t2] is DRAW:
                    if t2 == col:
                        color[m2, c2, t2] = col
                        que.append((m2, c2, t2))
                    else:
                        degree[m2, c2, t2] -= 1
                        if not degree[m2, c2, t2]:
                            color[m2, c2, t2] = 3 - t2
                            que.append((m2, c2, t2))
        return color[1, 2, 1]
