n, m = map(int, input().split())
Graph = [[float("inf")] * n for i in range(n)]
A, B, C = [], [], []
for i in range(n):
    Graph[i][i] = 0
for i in range(m):
    a, b, c = map(int, input().split())
    Graph[a - 1][b - 1] = c
    Graph[b - 1][a - 1] = c
    A.append(a - 1)
    B.append(b - 1)
    C.append(c)
for k in range(n):
    for i in range(n):
        for j in range(n):
            Graph[i][j] = min(Graph[i][j], Graph[i][k] + Graph[k][j])
ans = m
for i in range(m):
    for j in range(n):
        if Graph[j][A[i]] + C[i] == Graph[j][B[i]]:
            ans -= 1
            break
print(ans)
