class Solution:

    def catMouseGame(self, graph: List[List[int]]) -> int:

        def dp(mp, cp, turn):
            if turn >= N:
                return 0
            if mp == 0:
                return 1
            if mp == cp:
                return 2
            if (mp, cp, turn) in memo:
                return memo[mp, cp, turn]
            res = 0
            if turn % 2 == 0:
                if any((dp(nxt, cp, turn + 1) == 1 for nxt in graph[mp])):
                    res = 1
                elif all((dp(nxt, cp, turn + 1) == 2 for nxt in graph[mp])):
                    res = 2
            elif any((dp(mp, nxt, turn + 1) == 2 for nxt in graph[cp] if nxt != 0)):
                res = 2
            elif all((dp(mp, nxt, turn + 1) == 1 for nxt in graph[cp] if nxt != 0)):
                res = 1
            memo[mp, cp, turn] = res
            return res
        N = len(graph)
        memo = {}
        return dp(1, 2, 0)
