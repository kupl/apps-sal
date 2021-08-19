class Solution:
    # minimax
    # https://www.youtube.com/watch?v=WJ7uqznd_4s
    def catMouseGame(self, graph: List[List[int]]) -> int:
        memo = {}

        def mouse_play(key, cat, mouse, turn):
            if any(v == 0 for v in graph[mouse]):
                memo[key] = 1
                return 1
            res = 2
            for nxt in graph[mouse]:
                # mouse reach 0, mouse wins
                # mouse would not run int place cat holds now
                if nxt == cat:
                    continue
                tmp = move(cat, nxt, False)
                # if mouse win, directly break, mouse would always take the optimal solution
                if tmp == 1:
                    res = 1
                    break
                if tmp == 0:
                    res = 0
            memo[key] = res

            return res

        def cat_play(key, cat, mouse, turn):
            if any(v == mouse for v in graph[cat]):
                memo[key] = 2
                return 2
            res = 1
            for nxt in graph[cat]:
                # if nxt == mouse:
                #     memo[key] = 2
                #     return 2
                # cat can not enter hole
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
        DRAW, MOUSE, CAT = 0, 1, 2

        def parents(m, c, t):
            if t == MOUSE:
                for c2 in graph[c]:
                    if c2:  # cat can not enter 0
                        yield m, c2, 3 - t
            if t == CAT:
                for m2 in graph[m]:
                    yield m2, c, 3 - t

        color, degree = collections.defaultdict(int), {}

        # (mouse, cat, turn), got the parents/children of this node, [[2,3],...], since the graph is un-directed
        # you can say 2,3 -> 0 (parents) or 0 -> (2,3) children, here we regard it as parents
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
            m, c, t = que.pop()
            col = color[m, c, t]
            # for (m,c,t)'s parents, if
            for m2, c2, t2 in parents(m, c, t):
                if color[m2, c2, t2] is DRAW:
                    if t2 == col:  # mouse 's turn and it goes to MOUSE, or cat's turn, go to CAT
                        color[m2, c2, t2] = col
                        que.append((m2, c2, t2))
                    else:
                        # (m2,c2,t2) is (m,c,t)'s parent, if cat went to MOUSE, or mouse went to CAT,
                        # this is a lose situation, degree -=1, which means we have a losing for its
                        # one children, if all chidren are losing for this parent, ie, degree == 0
                        # then we add it to queue
                        degree[m2, c2, t2] -= 1
                        if not degree[m2, c2, t2]:
                            color[m2, c2, t2] = 3 - t2
                            que.append((m2, c2, t2))

        return color[1, 2, 1]
