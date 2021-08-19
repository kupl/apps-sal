class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        N = len(graph)

        # What nodes could play their turn to
        # arrive at node (mouse, cat, turn) ?
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

        # degree[node] : the number of neutral children of this node
        degree = {}
        for mouse in range(N):
            for cat in range(N):
                degree[mouse, cat, MOUSE] = len(graph[mouse])
                degree[mouse, cat, CAT] = len(graph[cat]) - (0 in graph[cat])  # cat can not be at hole 0

        # enqueued : all nodes that are colored
        queue = collections.deque([])
        for cat in range(N):
            for turn in [MOUSE, CAT]:
                # color MOUSE for all node with mouse=0
                mouse = 0
                colors[mouse, cat, turn] = MOUSE
                queue.append((mouse, cat, turn, MOUSE))
                # color CAT for all node with mouse = cat !=0, cat can not be at hole 0
                if cat > 0:
                    mouse = cat
                    colors[mouse, cat, turn] = CAT
                    queue.append((mouse, cat, turn, CAT))

        # percolate
        while queue:
            mouse, cat, turn, color = queue.popleft()
            for prev_mouse, prev_cat, prev_turn in parents(mouse, cat, turn):
                # if this parent is not colored :
                if colors[prev_mouse, prev_cat, prev_turn] is DRAW:
                    # if the parent can make a winning move (ie. mouse to MOUSE), do so
                    if prev_turn == color:  # winning move
                        colors[prev_mouse, prev_cat, prev_turn] = color
                        queue.append((prev_mouse, prev_cat, prev_turn, color))
                        if prev_mouse == 1 and prev_cat == 2 and prev_turn == MOUSE:
                            return color
                    # else, this parent has degree[parent]--, and enqueue if all children
                    # of this parent are colored as losing moves
                    else:
                        degree[prev_mouse, prev_cat, prev_turn] -= 1
                        if degree[prev_mouse, prev_cat, prev_turn] == 0:
                            colors[prev_mouse, prev_cat, prev_turn] = 3 - prev_turn
                            queue.append((prev_mouse, prev_cat, prev_turn, 3 - prev_turn))
                            if prev_mouse == 1 and prev_cat == 2 and prev_turn == MOUSE:
                                return color

        return colors[1, 2, 1]  # mouse at 1, cat at 2, MOUSE turn
