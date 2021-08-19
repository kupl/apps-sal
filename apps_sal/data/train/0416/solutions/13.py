class Solution:

    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        CAT_TURN = CAT_WIN = 2
        MOUSE_TURN = MOUSE_WIN = 1
        DRAW = 0
        outcome = defaultdict(int)
        degree = {}
        for cat in range(n):
            cat_neighbour_has_zero = 1 if 0 in graph[cat] else 0
            for mouse in range(n):
                degree[mouse, cat, 1] = len(graph[mouse])
                degree[mouse, cat, 2] = len(graph[cat]) - cat_neighbour_has_zero
        queue = deque()
        for cat in range(n):
            for turn in [MOUSE_TURN, CAT_TURN]:
                outcome[0, cat, turn] = MOUSE_WIN
                queue.append((0, cat, turn, MOUSE_WIN))
                if cat > 0:
                    outcome[cat, cat, turn] = CAT_WIN
                    queue.append((cat, cat, turn, CAT_WIN))

        def previous(mouse, cat, turn):
            if turn == MOUSE_TURN:
                for prev_cat in graph[cat]:
                    if prev_cat:
                        yield (mouse, prev_cat, 3 - turn)
            else:
                for prev_mouse in graph[mouse]:
                    yield (prev_mouse, cat, 3 - turn)
        while queue:
            (mouse, cat, turn, final_outcome) = queue.popleft()
            for (prev_mouse, prev_cat, prev_turn) in previous(mouse, cat, turn):
                if outcome[prev_mouse, prev_cat, prev_turn] == DRAW:
                    if prev_turn == final_outcome:
                        outcome[prev_mouse, prev_cat, prev_turn] = final_outcome
                        queue.append((prev_mouse, prev_cat, prev_turn, final_outcome))
                    else:
                        degree[prev_mouse, prev_cat, prev_turn] -= 1
                        if degree[prev_mouse, prev_cat, prev_turn] == 0:
                            outcome[prev_mouse, prev_cat, prev_turn] = 3 - prev_turn
                            queue.append((prev_mouse, prev_cat, prev_turn, 3 - prev_turn))
        return outcome[1, 2, 1]
