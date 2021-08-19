from collections import deque

h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

q = deque()
q.append((0, 0, 0))
check = [[0] * w for _ in range(h)]

flag = False
while q:
    y, x, d = q.popleft()
    if y == h - 1 and x == w - 1:
        g = d
        flag = True
        break
    if check[y][x] == 0:
        check[y][x] = 1
        for xdx, ydy in zip((x, x, x + 1, x - 1), (y + 1, y - 1, y, y)):
            if (0 <= xdx < w) and (0 <= ydy < h):
                if check[ydy][xdx] == 0 and s[ydy][xdx] == '.':
                    q.append((ydy, xdx, d + 1))
ss = 0
for i in s:
    ss += i.count('#')
print(h * w - ss - d - 1 if flag else -1)
