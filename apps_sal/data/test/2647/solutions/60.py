from collections import deque

H, W = map(int, input().split())
w = "#" * (W + 2)
white = 0
S = [w]
for _ in range(H):
    wwww = input()
    white += wwww.count(".")
    S.append("#" + wwww + "#")
S.append(w)

m = [[10**10] * (W + 2) for _ in range(H + 2)]

q = deque([[1, 1]])
d = ((-1, 0), (0, -1), (0, 1), (1, 0))

m[1][1] = 0

while q:
    y, x = q.popleft()
    p = m[y][x]
    for dx, dy in d:
        xx = x + dx
        yy = y + dy
        if S[yy][xx] == "#":
            continue
        if m[yy][xx] > p + 1:
            m[yy][xx] = p + 1
            q.append([yy, xx])

if m[H][W] == 10**10:
    print(-1)
else:
    print(white - m[H][W] - 1)
