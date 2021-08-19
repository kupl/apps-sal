def R():
    return map(int, input().split())


(n, m, k) = R()
a = [list(R()) for _ in range(n)]
b = [[0] * m for _ in range(n)]
c = [0] * m
for i in range(k):
    (x, y) = R()
    x -= 1
    y -= 1
    c[y] += 1
    b[x][y] += 1
print(' '.join(map(str, (sum((c[j] - b[i][j] for j in range(m) if a[i][j] == 1)) for i in range(n)))))
