from collections import deque
H, W = map(int, input().split())
f = [[s == "." for s in input()] for h in range(H)]
v = [[-1 for w in range(W)] for h in range(H)]

ans = 0
dh = [-1, 0, 0, 1]
dw = [0, 1, -1, 0]
for h in range(H):
    for w in range(W):
        if not f[h][w]:
            continue
        tmp = 0
        v = [[-1 for w in range(W)] for h in range(H)]
        Q = deque([(h, w)])
        v[h][w] = 0
        while Q:
            nh, nw = Q.popleft()
            for i in range(4):
                if 0 <= nh + dh[i] < H and 0 <= nw + dw[i] < W and f[nh + dh[i]][nw + dw[i]] and v[nh + dh[i]][nw + dw[i]] == -1:
                    v[nh + dh[i]][nw + dw[i]] = v[nh][nw] + 1
                    tmp = v[nh + dh[i]][nw + dw[i]]
                    Q.append((nh + dh[i], nw + dw[i]))
        ans = max(ans, tmp)
print(ans)
