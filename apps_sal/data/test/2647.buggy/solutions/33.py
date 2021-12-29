dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)
(H, W) = list(map(int, input().split()))
S = [input() for i in range(H)]
S_check = [[False] * W for _ in range(H)]
start = (0, 0, 1)
goal = (H - 1, W - 1)
Q = []
Q.append(start)
step = 0
is_reached = False
while Q:
    current = Q.pop(0)
    step = current[2]
    for i in range(4):
        next_pos = (current[0] + dx[i], current[1] + dy[i])
        if next_pos[0] < 0 or next_pos[0] > H - 1 or next_pos[1] < 0 or (next_pos[1] > W - 1):
            continue
        elif S_check[next_pos[0]][next_pos[1]]:
            continue
        elif next_pos == goal:
            is_reached = True
            break
        elif S[next_pos[0]][next_pos[1]] == '#':
            continue
        else:
            S_check[next_pos[0]][next_pos[1]] = True
            Q.append((next_pos[0], next_pos[1], step + 1))
    if is_reached:
        break
cnt = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            cnt += 1
ans = -1
if is_reached:
    ans = H * W - step - 1 - cnt
print(ans)
