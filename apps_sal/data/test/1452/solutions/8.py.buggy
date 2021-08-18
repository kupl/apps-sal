h, w = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

grid = [[-1] * w for i in range(h)]
for i in range(h):
    if a[i] == 0:
        grid[i][0] = 0
        continue
    for j in range(a[i]):
        grid[i][j] = 1
    if 0 <= a[i] < w:
        grid[i][a[i]] = 0

for j in range(w):
    if b[j] == 0:
        if grid[0][j] != 1:
            grid[0][j] = 0
        else:
            print(0)
            return
        continue
    for i in range(b[j]):
        if grid[i][j] != 0:
            grid[i][j] = 1
        else:
            print(0)
            return
    if 0 <= b[j] < h:
        if grid[b[j]][j] != 1:
            grid[b[j]][j] = 0
        else:
            print(0)
            return

MOD = 10**9 + 7
ans = 1
for i in range(h):
    for j in range(w):
        if grid[i][j] == -1:
            ans *= 2
            ans %= MOD
print(ans)
