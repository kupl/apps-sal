(n, m) = map(int, input().split())
L = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    (a, b) = map(int, input().split())
    L[a - 1][b - 1] += 1
    L[b - 1][a - 1] += 1
for i in range(n):
    print(sum(L[i]))
