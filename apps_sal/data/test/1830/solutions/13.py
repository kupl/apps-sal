read = lambda: list(map(int, input().split()))
n, m = read()
ans = [0] * m
dx = [0] * (n + 1)
dy = [0] * (n + 1)
cur = n ** 2
kx = ky = 0
for i in range(m):
    x, y = read()
    if dx[x] == 0 and dy[y] == 0:
        cur = cur - n - n + kx + ky + 1
        kx += 1
        ky += 1
        dx[x] = 1
        dy[y] = 1
    elif dx[x] == 0 and dy[y] == 1:
        cur = cur - n + ky
        kx += 1
        dx[x] = 1
    elif dx[x] == 1 and dy[y] == 0:
        cur = cur - n + kx
        ky += 1
        dy[y] = 1
    ans[i] = cur
print(*ans)

