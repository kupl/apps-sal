class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        @lru_cache(None)
        def search(t, x, y):
            if t == len(graph) * 2: 
                return 0
            if x == y:
                return 2
            if x == 0:
                return 1
            
            if (t%2==0):
                flag = True
                for i in range(len(graph[x])):
                    nxt = search(t+1, graph[x][i], y)
                    if nxt == 1:
                        return 1
                    elif nxt!=2:
                        flag = False
                if flag:
                    return 2
                return 0
            else:
                flag = True
                for i in range(len(graph[y])):
                    if graph[y][i]!=0:
                        nxt = search(t + 1, x, graph[y][i])
                        if nxt ==2:
                            return 2
                        elif nxt != 1:
                            flag=False
                if flag:
                    return 1
                else:
                    return 0
        n = len(graph)

        return search(0, 1, 2)

