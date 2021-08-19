from functools import lru_cache
from collections import defaultdict


class Solution:

    def catMouseGame(self, graph: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i in range(len(graph)):
            for j in graph[i]:
                adj[i].append(j)
                adj[j].append(i)

        @lru_cache(None)
        def search(m: int, c: int, turn: int, time: int) -> int:
            if m == 0:
                return 1
            elif m == c:
                return 2
            elif time >= 50:
                return 0
            if turn == 0:
                can_draw = False
                for y in adj[m]:
                    res = search(y, c, 1 - turn, time + 1)
                    if res == 1:
                        return 1
                    elif res == 0:
                        can_draw = True
                return 0 if can_draw else 2
            else:
                can_draw = False
                for y in adj[c]:
                    if y == 0:
                        continue
                    res = search(m, y, 1 - turn, time + 1)
                    if res == 2:
                        return 2
                    elif res == 0:
                        can_draw = True
                return 0 if can_draw else 1
        return search(1, 2, 0, 0)
