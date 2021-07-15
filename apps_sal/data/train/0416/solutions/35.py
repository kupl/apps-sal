class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        N = len(graph)
        lim = 2 * N
        
        @lru_cache(maxsize=None)
        def _visit(state: Tuple[int, int, int], t):
            if t >= lim:
                return 0

            x, y, p = state
            if x == 0:
                return 1
            elif x == y :
                return 2
            
            if p == 1:
                it = (_visit((n, y, 2), t+1) for n in graph[x])
            else:
                it = (_visit((x, n, 1), t+1) for n in graph[y] if n != 0)
            
            update = 1 if p == 2 else 2
            
            for v in it:
                if v == p:
                    return p
                elif v == 0:
                    update = 0
            
            return update

        r = _visit((1, 2, 1), 0)
        return r
