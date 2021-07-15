class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        cache = [[[-1] * (2 * n) for _ in range(n)] for _ in range(n)]
        def move(cat, mouse, t):
            if t == 2 * n:
                return 0
            elif mouse == 0:
                return 1
            elif cat == mouse:
                return 2
            if cache[cat][mouse][t] == -1:
                mouse_move = (t % 2) == 0
                if mouse_move:
                    best_result = 2
                    for pos in graph[mouse]:
                        result = move(cat, pos, t + 1)
                        if result == 1:
                            cache[cat][mouse][t] = 1
                            return 1
                        if result == 0:
                            best_result = 0
                else:
                    best_result = 1
                    for pos in graph[cat]:
                        if pos == 0:
                            continue
                        result = move(pos, mouse, t + 1)
                        if result == 2:
                            cache[cat][mouse][t] = 2
                            return 2
                        if result == 0:
                            best_result = 0
                cache[cat][mouse][t] = best_result
            return cache[cat][mouse][t]
        return move(2, 1, 0)
