class Solution:
    def catMouseGame(self, g: List[List[int]]) -> int:
        
        # status: current_mouse_position, current_cat_position, move_next(0 : mouse, 1 : cat)
        
        for i in range(len(g)):
            g[i] = set(g[i])
        
        out_degree = {}
        for mouse in range(len(g)):
            for cat in range(1, len(g)):
                out_degree[(mouse, cat, 0)] = len(g[mouse])
                out_degree[(mouse, cat, 1)] = len(g[cat]) - (0 in g[cat])
        
        
        visit = set()
        status_result = deque()
        for cat in range(1, len(g)):
            status_result.append([0, cat, 1, 1])
            status_result.append([0, cat, 0, 1])
            visit.add((0, cat, 1))
            visit.add((0, cat, 0))
            
        for mouse in range(1, len(g)):
            status_result.append([mouse, mouse, 0, 2])
            status_result.append([mouse, mouse, 1, 2])
            visit.add((mouse, mouse, 0))
            visit.add((mouse, mouse, 1))
        
        idx = 0
        while len(status_result):
            idx += 1
            # print(status_result)
            mouse, cat, move_next, result = status_result.popleft()
            if mouse == 1 and cat == 2 and move_next == 0:
                return result
            move_prev = 1 - move_next
            if move_prev == 0:
                for p in g[mouse]:
                    if result == 1:
                        if (p, cat, 0) not in visit:
                            status_result.append([p, cat, 0, 1])
                            visit.add((p, cat, 0))
                    else:
                        out_degree[(p, cat, 0)] -= 1
                        if out_degree[(p, cat, 0)] == 0 and (p, cat, 0) not in visit:
                            status_result.append([p, cat, 0, 2])
                            visit.add((p, cat, 0))
            elif move_prev == 1:
                for p in g[cat]:
                    if p != 0:
                        if result == 2:
                            if (mouse, p, 1) not in visit:
                                status_result.append([mouse, p, 1, 2])
                                visit.add((mouse, p, 1))
                        else:
                            out_degree[(mouse, p, 1)] -= 1
                            if out_degree[(mouse, p, 1)] == 0 and (mouse, p, 1) not in visit:
                                status_result.append([mouse, p, 1, 1])
                                visit.add((mouse, p, 1))
        return 0
                    
                    

