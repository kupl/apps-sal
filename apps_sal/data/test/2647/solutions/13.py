from _collections import deque


def bfs():  # 最短経路を求める　→　白マスの数から最短経路を引く
    que = deque([])
    que.append((0, 0))
    dh = [-1, 0, 1, 0]
    dw = [0, -1, 0, 1]
    d = [[float("inf")] * w for _ in range(h)]
    d[0][0] = 0
    while que:
        p = que.popleft()
        if p[0] == h - 1 and p[1] == w - 1:
            break
        for i in range(4):
            nh = p[0] + dh[i]
            nw = p[1] + dw[i]
            if 0 <= nh < h and 0 <= nw < w and d[nh][nw] == float("inf") and c[nh][nw] == '.':
                que.append((nh, nw))
                d[nh][nw] = 1 + d[p[0]][p[1]]
    return d[h - 1][w - 1]


h, w = list(map(int, input().split()))
c = [list(input()) for _ in range(h)]
count = 0  # 白マスの数
for i in range(h):
    for j in range(w):
        if c[i][j] == '.':
            count += 1

mi = bfs()

if 0 < mi < float("inf"):
    print((count - mi - 1))
else:
    print((-1))
