class Solution:
    # O(n^4) time, O(n^3) space
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        edges = defaultdict(list)
        for i, nbrs in enumerate(graph):
            for nbr in nbrs:
                edges[i].append(nbr)
                edges[nbr].append(i)

        # cache = {}
        @lru_cache(None)
        def can_win(cat_pos, mouse_pos, remaining_moves, is_cats_turn):
            # state = cat_pos, mouse_pos, is_cats_turn, remaining_moves
            # if state in cache:
            #     return cache[state]
            if mouse_pos == 0:  # mouse wins
                if is_cats_turn:
                    # cache[state] = -1
                    return -1
                # cache[state] = 1
                return 1
            if cat_pos == mouse_pos:  # cat wins
                if is_cats_turn:
                    # cache[state] = 1
                    return 1
                # cache[state] = -1
                return -1
            if remaining_moves == 0:  # draw
                # cache[state] = 0
                return 0

            opponents_worst_case = 1
            if is_cats_turn:
                for nbr in edges[cat_pos]:
                    if nbr == 0:
                        continue
                    opponents_worst_case = min(
                        opponents_worst_case, can_win(nbr, mouse_pos, remaining_moves - 1, not is_cats_turn)
                    )
            else:
                for nbr in edges[mouse_pos]:
                    opponents_worst_case = min(
                        opponents_worst_case, can_win(cat_pos, nbr, remaining_moves - 1, not is_cats_turn)
                    )

            # cache[state] = -opponents_worst_case
            return -opponents_worst_case

        mouse_outcome = can_win(2, 1, 2 * n, False)
        if mouse_outcome == 1:
            return 1
        if mouse_outcome == -1:
            return 2
        return 0

#     def catMouseGame(self, graph: List[List[int]]) -> int:
#         n = len(graph)
#         edges = defaultdict(list)
#         for i, nbrs in enumerate(graph):
#             for nbr in nbrs:
#                 edges[i].append(nbr)
#                 edges[nbr].append(i)

#         q = [(1, 2)]
#         seen = set()
#         seen.add((1, 2))
#         step = 0
#         is_mouses_turn = True
#         while q:
#             if step > 2 * n:
#                 break
#             # last round is cat's turn
#             if is_mouses_turn and any(cat_pos == mouse_pos for mouse_pos, cat_pos in q):
#                 return 2
#             # last round is mouse's turn
#             if not is_mouses_turn and any(mouse_pos == 0 for mouse_pos, _ in q):
#                 return 1

#             q2 = []
#             for mouse_pos, cat_pos in q:
#                 if is_mouses_turn:
#                     for nbr in edges[mouse_pos]:
#                         next_state = nbr, cat_pos
#                         if next_state in seen:
#                             continue
#                         q2.append(next_state)
#                         seen.add(next_state)
#                 else:
#                     for nbr in edges[cat_pos]:
#                         if nbr == 0:
#                             continue
#                         next_state = mouse_pos, nbr
#                         if next_state in seen:
#                             continue
#                         q2.append(next_state)
#                         seen.add(next_state)
#             q = q2
#             step += 1
#             is_mouses_turn = not is_mouses_turn

#         return 0

    def catMouseGame(self, graph: List[List[int]]) -> int:
        @lru_cache(None)
        def search(t, x, y):
            if t == len(graph) * 2:
                return 0
            if x == y:
                return 2
            if x == 0:
                return 1
            if (t % 2 == 0):  # mouse's turn. Mouse will win if the mouse can find any winable node for the next step. If all the next step is winable for cats, then mouse lose.
                if any(search(t + 1, x_nxt, y) == 1 for x_nxt in graph[x]):
                    return 1
                if all(search(t + 1, x_nxt, y) == 2 for x_nxt in graph[x]):
                    return 2
                return 0
            else:  # cat's turn
                if any(search(t + 1, x, y_nxt) == 2 for y_nxt in graph[y] if y_nxt != 0):
                    return 2
                if all(search(t + 1, x, y_nxt) == 1 for y_nxt in graph[y] if y_nxt != 0):
                    return 1
                return 0
        return search(0, 1, 2)
