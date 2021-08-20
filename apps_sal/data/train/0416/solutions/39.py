class Solution:

    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        edges = defaultdict(list)
        for (i, nbrs) in enumerate(graph):
            for nbr in nbrs:
                edges[i].append(nbr)
                edges[nbr].append(i)

        @lru_cache(None)
        def can_win(cat_pos, mouse_pos, remaining_moves, is_cats_turn):
            if mouse_pos == 0:
                if is_cats_turn:
                    return -1
                return 1
            if cat_pos == mouse_pos:
                if is_cats_turn:
                    return 1
                return -1
            if remaining_moves == 0:
                return 0
            opponents_worst_case = 1
            if is_cats_turn:
                for nbr in edges[cat_pos]:
                    if nbr == 0:
                        continue
                    opponents_worst_case = min(opponents_worst_case, can_win(nbr, mouse_pos, remaining_moves - 1, not is_cats_turn))
            else:
                for nbr in edges[mouse_pos]:
                    opponents_worst_case = min(opponents_worst_case, can_win(cat_pos, nbr, remaining_moves - 1, not is_cats_turn))
            return -opponents_worst_case
        mouse_outcome = can_win(2, 1, 2 * n, False)
        if mouse_outcome == 1:
            return 1
        if mouse_outcome == -1:
            return 2
        return 0

    def catMouseGame(self, graph: List[List[int]]) -> int:

        @lru_cache(None)
        def search(t, x, y):
            if t == len(graph) * 2:
                return 0
            if x == y:
                return 2
            if x == 0:
                return 1
            if t % 2 == 0:
                if any((search(t + 1, x_nxt, y) == 1 for x_nxt in graph[x])):
                    return 1
                if all((search(t + 1, x_nxt, y) == 2 for x_nxt in graph[x])):
                    return 2
                return 0
            else:
                if any((search(t + 1, x, y_nxt) == 2 for y_nxt in graph[y] if y_nxt != 0)):
                    return 2
                if all((search(t + 1, x, y_nxt) == 1 for y_nxt in graph[y] if y_nxt != 0)):
                    return 1
                return 0
        return search(0, 1, 2)
