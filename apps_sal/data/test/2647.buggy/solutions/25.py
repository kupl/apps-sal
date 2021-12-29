from collections import deque
(H, W) = list(map(int, input().split()))
S = [list(input()) for _ in range(H)]


def get_next(x, y, costs, S, cost):
    ans = list()
    if x != 0 and costs[x - 1][y] == -1 and (S[x - 1][y] == '.'):
        ans.append([x - 1, y])
        costs[x - 1][y] = cost + 1
    if x != H - 1 and costs[x + 1][y] == -1 and (S[x + 1][y] == '.'):
        ans.append([x + 1, y])
        costs[x + 1][y] = cost + 1
    if y != 0 and costs[x][y - 1] == -1 and (S[x][y - 1] == '.'):
        ans.append([x, y - 1])
        costs[x][y - 1] = cost + 1
    if y != W - 1 and costs[x][y + 1] == -1 and (S[x][y + 1] == '.'):
        ans.append([x, y + 1])
        costs[x][y + 1] = cost + 1
    return ans


costs = [[-1 for _ in range(W)] for _ in range(H)]
costs[0][0] = 0
q = deque()
q.append([0, 0])
while len(q) and costs[H - 1][W - 1] == -1:
    now = q.popleft()
    nxt = get_next(now[0], now[1], costs, S, costs[now[0]][now[1]])
    for dot in nxt:
        q.append([dot[0], dot[1]])
fin_cost = costs[H - 1][W - 1]
if fin_cost == -1:
    print(-1)
else:
    w_cnt = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                w_cnt += 1
    print(w_cnt - fin_cost - 1)
