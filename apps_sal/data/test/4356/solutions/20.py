n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]
b = [list(input()) for _ in range(m)]
for i in range(0, n - m + 1):
    for j in range(0, n - m + 1):
        p = [a[x][i:i + m] for x in range(j, j + m)]
        ok = 0
        for h in range(m):
            x, y = p[h], b[h]
            for k in range(m):
                if x[k] != y[k]:
                    ok += 1
        if ok == 0:
            print('Yes')
            return
print('No')
