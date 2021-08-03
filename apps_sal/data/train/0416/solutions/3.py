class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = 0
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                n = max(n, graph[i][j])

        status = [[[0] * 3 for i in range(n + 1)] for j in range(n + 1)]  # s[m][c][t]

        queue = []
        for i in range(1, n + 1):
            status[i][i][1] = 2
            status[i][i][2] = 2
            status[0][i][1] = 1
            status[0][i][2] = 1
            queue.append((i, i, 1))
            queue.append((i, i, 2))
            queue.append((0, i, 1))
            queue.append((0, i, 2))

        while queue:
            next_queue = []
            for element in queue:
                mouse = element[0]
                cat = element[1]
                turn = element[2]
                if turn == 1:
                    for cat_pre in graph[cat]:
                        if cat_pre == 0:
                            continue
                        if status[mouse][cat_pre][2] == 0:
                            status[mouse][cat_pre][2] = 1
                            for cat_alt in graph[cat_pre]:
                                if cat_alt == 0:
                                    continue
                                if status[mouse][cat_alt][1] == 2:
                                    status[mouse][cat_pre][2] = 2
                                    break
                                elif status[mouse][cat_alt][1] == 0:
                                    status[mouse][cat_pre][2] = 0
                            if status[mouse][cat_pre][2] > 0:
                                next_queue.append((mouse, cat_pre, 2))
                else:
                    for mouse_pre in graph[mouse]:
                        if status[mouse_pre][cat][1] == 0:
                            status[mouse_pre][cat][1] = 2
                            for mouse_alt in graph[mouse_pre]:
                                if status[mouse_alt][cat][2] == 1:
                                    status[mouse_pre][cat][1] = 1
                                    break
                                elif status[mouse_alt][cat][2] == 0:
                                    status[mouse_pre][cat][1] = 0
                            if status[mouse_pre][cat][1] > 0:
                                next_queue.append((mouse_pre, cat, 1))
            queue = next_queue

        return status[1][2][1]
