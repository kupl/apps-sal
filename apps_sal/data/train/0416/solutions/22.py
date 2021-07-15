from functools import lru_cache


class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        MOUSE, CAT, DRAW = 1, 2, 0
        
        @lru_cache(None)
        def winner(mouse, cat, turn):
            if turn >= len(graph)*2:
                return DRAW
            if turn%2 == 0:
                if 0 in graph[mouse]:
                    return MOUSE
                answer = CAT
                for i in graph[mouse]:
                    if i == cat:
                        continue
                    result = winner(i, cat, turn+1)
                    if result == MOUSE:
                        return MOUSE
                    if result == DRAW:
                        answer = DRAW
                return answer
            else:
                if mouse in graph[cat]:
                    return CAT
                answer = MOUSE
                for i in graph[cat]:
                    if i == 0:
                        continue
                    result = winner(mouse, i, turn+1)
                    if result == CAT:
                        return CAT
                    if result == DRAW:
                        answer = DRAW
                return answer
        
        return winner(1, 2, 0)
