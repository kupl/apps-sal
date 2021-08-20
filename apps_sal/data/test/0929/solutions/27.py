(h, w) = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
n = 0
ans = []
b = []
for i in range(h):
    for j in range(w):
        b.append((i, j if i % 2 == 0 else w - j - 1))
for i in range(h * w - 1):
    (y, x) = b[i]
    if a[y][x] % 2 == 0:
        continue
    a[y][x] -= 1
    n += 1
    (ny, nx) = b[i + 1]
    a[ny][nx] += 1
    ans.append('{} {} {} {}'.format(str(y + 1), str(x + 1), str(ny + 1), str(nx + 1)))
print(n)
print('\n'.join(ans))
