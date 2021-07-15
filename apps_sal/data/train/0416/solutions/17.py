
class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        MOUSE = 1
        CAT = 2
        DRAW = 0
        states = collections.defaultdict(lambda: DRAW)
        
        
        
        n = len(graph) 
        for i in range(1, n):
            states[i, i, MOUSE] = CAT
            states[i, i, CAT] = CAT
            states[0, i, MOUSE] = MOUSE
            states[0, i, CAT] = MOUSE
            
        draws = dict()
        for mouse in range(n):
            for cat in range(1, n):
                draws[mouse, cat, CAT] = len(graph[cat]) - (0 in graph[cat])
                draws[mouse, cat, MOUSE] = len(graph[mouse])
                    
                    
                        
                        
        def neighbor(mouse, cat, turn):
            prev_turn = CAT if turn == MOUSE else MOUSE
            if prev_turn == MOUSE:
                for prev_mouse in graph[mouse]:
                    yield prev_mouse, cat, prev_turn
            else:
                for prev_cat in graph[cat]:
                    if prev_cat != 0:
                        yield mouse, prev_cat, prev_turn
        
        queue = collections.deque()
        for state in states.keys():
            queue.append(state)
        
        while len(queue) > 0:
            state = queue.popleft()
            mouse, cat, turn = state
            win = states[state]
            
            for prev_state in neighbor(*state):
                prev_mouse, prev_cat, prev_turn = prev_state
                if states[prev_state] != DRAW:
                    continue
                elif prev_turn == win:
                    states[prev_state] = win
                    queue.append(prev_state)
                else:
                    draws[prev_state] -= 1
                    if draws[prev_state] == 0:
                        states[prev_state] = turn
                        queue.append(prev_state)
                
        return states[1, 2, MOUSE]
