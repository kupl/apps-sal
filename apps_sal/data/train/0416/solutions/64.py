class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        # return 1
        n = len(graph)
        states = [[[0, 0] for _ in range(n)] for _ in range(n)]  # [mouse][cat][whose_turn (m/c)]
        for i in range(1, n):
            # mosue turn is 0, cat is 1
            states[0][i][0] = -1
            states[0][i][1] = -1
            states[i][i][0] = 1
            states[i][i][1] = 1

        # cnt = 0
        get_updated = False
        for _ in range(2 * n):

            get_updated = False

            for mouse in range(1, n):
                for cat in range(1, n):
                    for turn in range(2):
                        if mouse != cat and mouse != 0:
                            if turn == 0:
                                adj = graph[mouse]
                                res = float('inf')
                                for node in adj:
                                    res = min(res, states[node][cat][1])
                                    # cnt += 1

                                if states[mouse][cat][turn] != res:
                                    get_updated = True

                                states[mouse][cat][turn] = res
                            else:
                                adj = graph[cat]
                                res = float('-inf')
                                for node in adj:
                                    if node != 0:
                                        res = max(res, states[mouse][node][0])
                                        # cnt += 1

                                if states[mouse][cat][turn] != res:
                                    get_updated = True

                                    states[mouse][cat][turn] = res
            if not get_updated:
                break

        # print(states[3][3][0])
        # print(cnt)

        res = states[1][2][0]
        # res = self.play(1, 2, 0, graph, states)
        if res < 0:
            return 1
        if res > 0:
            return 2
        return 0
