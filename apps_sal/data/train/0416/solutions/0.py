class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        N = len(graph)

        def parents(mouse, cat, turn):
            prev_turn = 3 - turn
            if prev_turn == MOUSE:
                for m2 in graph[mouse]:
                    yield m2, cat, prev_turn
            else:
                for c2 in graph[cat]:
                    if c2:
                        yield mouse, c2, prev_turn

        DRAW, MOUSE, CAT = 0, 1, 2
        colors = collections.defaultdict(int)

        degree = {}
        for mouse in range(N):
            for cat in range(N):
                degree[mouse, cat, MOUSE] = len(graph[mouse])
                degree[mouse, cat, CAT] = len(graph[cat]) - (0 in graph[cat])

        queue = collections.deque([])
        for cat in range(N):
            for turn in [MOUSE, CAT]:
                mouse = 0
                colors[mouse, cat, turn] = MOUSE
                queue.append((mouse, cat, turn, MOUSE))
                if cat > 0:
                    mouse = cat
                    colors[mouse, cat, turn] = CAT
                    queue.append((mouse, cat, turn, CAT))

        while queue:
            mouse, cat, turn, color = queue.popleft()
            for prev_mouse, prev_cat, prev_turn in parents(mouse, cat, turn):
                if colors[prev_mouse, prev_cat, prev_turn] is DRAW:
                    if prev_turn == color:
                        colors[prev_mouse, prev_cat, prev_turn] = color
                        queue.append((prev_mouse, prev_cat, prev_turn, color))
                        if prev_mouse == 1 and prev_cat == 2 and prev_turn == MOUSE:
                            return color
                    else:
                        degree[prev_mouse, prev_cat, prev_turn] -= 1
                        if degree[prev_mouse, prev_cat, prev_turn] == 0:
                            colors[prev_mouse, prev_cat, prev_turn] = 3 - prev_turn
                            queue.append((prev_mouse, prev_cat, prev_turn, 3 - prev_turn))
                            if prev_mouse == 1 and prev_cat == 2 and prev_turn == MOUSE:
                                return color

        return colors[1, 2, 1]
