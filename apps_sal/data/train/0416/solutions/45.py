from functools import lru_cache
class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        @lru_cache(None)
        def search(t, x, y):
            if t == len(graph) * 2: return 0
            if x == y: return 2
            if x == 0:return 1
            if (t%2==0):# mouse's turn. Mouse will win if the mouse can find any winable node for the next step. If all the next step is winable for cats, then mouse lose.
                if any(search(t+1, x_nxt, y)==1 for x_nxt in graph[x]):return 1
                if all(search(t+1, x_nxt, y)==2 for x_nxt in graph[x]):return 2
                return 0
            else:# cat's turn
                if any(search(t+1, x, y_nxt)==2 for y_nxt in graph[y] if y_nxt!=0):return 2
                if all(search(t+1, x, y_nxt)==1 for y_nxt in graph[y] if y_nxt!=0):return 1
                return 0
        return search(0, 1, 2)

