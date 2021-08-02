from collections import deque
H, W = list(map(int, input().split()))
S = [input() for _ in range(H)]

Q = deque([[0, 0]])
dist = [[-1] * W for _ in range(H)]
dist[0][0] = 0

while Q:
    h, w = Q.popleft()

    for nh, nw in [[h + 1, w], [h - 1, w], [h, w - 1], [h, w + 1]]:
        if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == "." and dist[nh][nw] == -1:
            dist[nh][nw] = dist[h][w] + 1
            Q.append([nh, nw])

if dist[H - 1][W - 1] == -1:
    print((-1))
else:
    ans = 0
    for s in S:
        ans += s.count(".")
    print((ans - dist[H - 1][W - 1] - 1))
