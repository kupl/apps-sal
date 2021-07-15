n, m, k = list(map(int, input().split()))
a, nc, mc = [list(map(int, input().split())) for i in range(n)], [0] * n, [0] * m
for i in range(k):
    x, y = list(map(int, input().split()))
    nc[x - 1] += 1
    mc[y - 1] += 1
print(' '.join(map(str, (sum(mc[j] for j in range(m) if a[i][j]) - nc[i] for i in range(n)))))

