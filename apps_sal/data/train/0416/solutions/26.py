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
                        yield mouse, prev_cat, 3 - turn
            else:
                for prev_mouse in graph[mouse]:
                    yield prev_mouse, cat, 3 - turn
         
        target = (1, 2, 1)
        while queue:
            mouse, cat, turn, final_outcome = queue.popleft()
            for prev_mouse, prev_cat, prev_turn in previous(mouse, cat, turn):
                if outcome[prev_mouse, prev_cat, prev_turn] == DRAW:
                    if prev_turn == final_outcome:
                        outcome[prev_mouse, prev_cat, prev_turn] = final_outcome
                        if (prev_mouse, prev_cat, prev_turn) == target:
                            return final_outcome
                        queue.append((prev_mouse, prev_cat, prev_turn, final_outcome))
                    else:
                        degree[prev_mouse, prev_cat, prev_turn] -= 1
                        if degree[prev_mouse, prev_cat, prev_turn] == 0:
                            if (prev_mouse, prev_cat, prev_turn) == target:
                                return 3 - prev_turn
                            outcome[prev_mouse, prev_cat, prev_turn] = 3 - prev_turn
                            queue.append((prev_mouse, prev_cat, prev_turn, 3 - prev_turn))
        return outcome[1, 2, 1]
        
        
        
        
#         # For n nodes, the possible longest path in the graph is n. If the cat can win, 
#         # its distance to the mouse should decrease, after decease n times if still doesn't 
#         # catch the mouse, and mouse haven't reach node 0 yet, means this is a draw
        
#         # it takes at most n for mouse to get to 0. At 2*n time, it means mouse take a 
#         # detour of at least n steps. It means that there should be at least a loop(size n) 
#         # or multiple loops of (size < n).
        
#         n = len(graph)
#         @lru_cache(None)
#         def move(cat, mouse, t):
#             # should be 2n but 0.8n also passes all tests
#             if t > int(0.8 * n):
#                 return 0
#             elif mouse == 0:
#                 return 1
#             elif cat == mouse:
#                 return 2
#             if t % 2 == 0:
#                 best_result = 2
#                 for pos in graph[mouse]:
#                     result = move(cat, pos, t + 1)
#                     if result == 1:
#                         return 1
#                     if result == 0:
#                         best_result = 0
#             else:
#                 best_result = 1
#                 for pos in graph[cat]:
#                     if pos == 0:
#                         continue
#                     result = move(pos, mouse, t + 1)
#                     if result == 2:
#                         return 2
#                     if result == 0:
#                         best_result = 0
#             return best_result
#         return move(2, 1, 0)
        
        
        
        
#         n = len(graph)
#         cache = [[[-1] * (2 * n) for _ in range(n)] for _ in range(n)]
#         def move(cat, mouse, t):
#             if t == 2 * n:
#                 return 0
#             elif mouse == 0:
#                 return 1
#             elif cat == mouse:
#                 return 2
#             if cache[cat][mouse][t] == -1:
#                 mouse_move = (t % 2) == 0
#                 if mouse_move:
#                     best_result = 2
#                     for pos in graph[mouse]:
#                         result = move(cat, pos, t + 1)
#                         if result == 1:
#                             cache[cat][mouse][t] = 1
#                             return 1
#                         if result == 0:
#                             best_result = 0
#                 else:
#                     best_result = 1
#                     for pos in graph[cat]:
#                         if pos == 0:
#                             continue
#                         result = move(pos, mouse, t + 1)
#                         if result == 2:
#                             cache[cat][mouse][t] = 2
#                             return 2
#                         if result == 0:
#                             best_result = 0
#                 cache[cat][mouse][t] = best_result
#             return cache[cat][mouse][t]
#         return move(2, 1, 0)

