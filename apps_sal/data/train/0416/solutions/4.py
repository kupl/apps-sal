class Solution:
    def catMouseGame(self, graph):
        CAT, MOUSE, n = 2, 1, len(graph)
        queue = []          # (cat, mouse, turn, winner)
        result = {}
        for i in range(n):
            for j in range(2):
                queue.append((i, 0, j, 1))
                result[(i, 0, j)] = 1
                if i > 0:
                    queue.append((i, i, j, 2))
                    result[(i, i, j)] = 2
                    queue.append((0, i, j, 1))
                    result[(0, i, j)] = 1

        cnt = {}
        for i in range(n):
            for j in range(n):
                cnt[(i, j, 0)] = len(graph[j])
                cnt[(i, j, 1)] = len(graph[i])

        while queue:
            cat, mouse, turn, winner = queue.pop()
            if turn == 1:   # cat move for next step, mouse move for last step
                if winner == 1:
                    for next_step in graph[mouse]:
                        if (cat, next_step, 1 - turn) not in result:
                            result[(cat, next_step, 1 - turn)] = winner
                            queue.append((cat, next_step, 1 - turn, winner))
                else:
                    for next_step in graph[mouse]:
                        if (cat, next_step, 1 - turn) not in result:
                            cnt[(cat, next_step, 1 - turn)] -= 1
                            if cnt[(cat, next_step, 1 - turn)] == 0:
                                result[(cat, next_step, 1 - turn)] = winner
                                queue.append((cat, next_step, 1 - turn, winner))
            else:
                if winner == 2:
                    for next_step in graph[cat]:
                        if next_step == 0:
                            continue
                        if (next_step, mouse, 1 - turn) not in result:
                            result[(next_step, mouse, 1 - turn)] = winner
                            queue.append((next_step, mouse, 1 - turn, winner))
                else:
                    for next_step in graph[cat]:
                        if next_step == 0:
                            continue
                        if (next_step, mouse, 1 - turn) not in result:
                            cnt[(next_step, mouse, 1 - turn)] -= 1
                            if cnt[(next_step, mouse, 1 - turn)] == 0:
                                result[(next_step, mouse, 1 - turn)] = winner
                                queue.append((next_step, mouse, 1 - turn, winner))
        if (2, 1, 0) in result:
            return result[(2, 1, 0)]
        return 0
