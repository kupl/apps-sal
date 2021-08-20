from collections import deque
import copy
(H, W) = list(map(int, input().split()))
ans = 0
distancelist = []
for i in range(H):
    maze = list(input())
    tmplst = [0] * W
    for j in range(W):
        if maze[j] == '#':
            tmplst[j] = -1
    distancelist.append(tmplst)
for x in range(H):
    for y in range(W):
        if distancelist[x][y] == -1:
            continue
        tmpdis = copy.deepcopy(distancelist)
        d = deque()
        start = [x, y]
        d.append(start)
        while d:
            (h, w) = d.popleft()
            now = tmpdis[h][w]
            for (i, j) in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                (dh, dw) = (h + i, w + j)
                if 0 <= dh < H and 0 <= dw < W:
                    if tmpdis[dh][dw] == 0 and [dh, dw] != start:
                        d.append([dh, dw])
                        tmpdis[dh][dw] = now + 1
            ans = max(now, ans)
print(ans)
