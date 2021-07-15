class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        @lru_cache(None)
        def search(t, x, y):
            if t == len(graph) * 2: return 0
            if x == y: return 2
            if x == 0:return 1
            if (t%2==0):# mouse's turn
                if any(search(t+1, graph[x][i], y)==1 for i in range(len(graph[x]))):
                    return 1
                if all(search(t+1, graph[x][i], y)==2 for i in range(len(graph[x]))):
                    return 2
                return 0
            else:# cat's turn
                if any(search(t+1, x, graph[y][i])==2 for i in range(len(graph[y])) if graph[y][i]!=0):
                    return 2
                if all(search(t + 1, x, graph[y][i])==1 for i in range(len(graph[y])) if graph[y][i]!=0): 
                    return 1
                return 0
        return search(0, 1, 2)

