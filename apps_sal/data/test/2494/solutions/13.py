from collections import deque


def bfs(K: int) -> list:
    hasChecked = [False] * (K + 1)
    cost_list = [0] * (K + 1)
    cost_list[1] = 1

    que = deque([(cost_list[1], 1)])

    while que:
        cost, res = que.popleft()
        if hasChecked[res]:
            continue

        hasChecked[res] = True
        cost_list[res] = cost

        if not hasChecked[10 * res % K]:
            que.appendleft((cost, 10 * res % K))

        if not hasChecked[(res + 1) % K]:
            que.append((cost + 1, (res + 1) % K))

    return cost_list


K = int(input())
cost_list = bfs(K)
print((cost_list[0]))
