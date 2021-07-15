N, Q = list(map(int, input().split()))

row = [N - 2] * (N + 2)
col = [N - 2] * (N + 2)
ans = (N - 2)**2

miRow = N
miCol = N

for _ in range(Q):
    q, x = list(map(int, input().split()))

    if q == 1:
        for i in range(x, miRow + 1):
            row[i] = min(row[i], miCol - 2)
        miRow = min(x, miRow)
        ans -= row[x]

    if q == 2:
        for i in range(x, miCol + 1):
            col[i] = min(col[i], miRow - 2)
        miCol = min(x, miCol)
        ans -= col[x]

print(ans)

