from collections import deque, defaultdict


class Solution:

    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        (DRAW, MOUSE, CAT) = (0, 1, 2)

        def parents(m, c, t):
            if t == MOUSE:
                return [(m, x, CAT) for x in graph[c] if x != 0]
            return [(x, c, MOUSE) for x in graph[m]]
        color = defaultdict(int)
        for t in (MOUSE, CAT):
            for x in range(n):
                color[0, x, t] = MOUSE
                if x != 0:
                    color[x, x, t] = CAT
        degree = {}
        for m in range(n):
            for c in range(n):
                degree[m, c, MOUSE] = len(parents(m, c, CAT))
                degree[m, c, CAT] = len(parents(m, c, MOUSE))
        q = deque()
        for (k, v) in color.items():
            q.append((*k, v))
        while q:
            (m, c, t, winner) = q.popleft()
            for (m2, c2, t2) in parents(m, c, t):
                if color[m2, c2, t2] != DRAW:
                    continue
                if t2 == winner:
                    color[m2, c2, t2] = winner
                    q.append((m2, c2, t2, winner))
                else:
                    degree[m2, c2, t2] -= 1
                    if degree[m2, c2, t2] == 0:
                        color[m2, c2, t2] = winner
                        q.append((m2, c2, t2, winner))
        return color[1, 2, 1]
