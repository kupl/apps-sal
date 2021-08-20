(n, m) = map(int, input().split())
li = [' ' * (m + 1)] + [' ' + input() for _ in range(n)]
(r, c) = ([[0 for i in range(m + 1)] for i in range(n + 1)], [[0 for i in range(m + 1)] for i in range(n + 1)])
q = int(input())
for i in range(1, n + 1):
    for j in range(1, m + 1):
        r[i][j] = r[i - 1][j] + r[i][j - 1] - r[i - 1][j - 1] + (li[i][j] == '.' and li[i][j - 1] == '.')
        c[i][j] = c[i - 1][j] + c[i][j - 1] - c[i - 1][j - 1] + (li[i][j] == '.' and li[i - 1][j] == '.')
for _ in range(q):
    (r1, c1, r2, c2) = map(int, input().split())
    print(c[r2][c2] - c[r1][c2] - c[r2][c1 - 1] + c[r1][c1 - 1] + r[r2][c2] - r[r2][c1] - r[r1 - 1][c2] + r[r1 - 1][c1])
