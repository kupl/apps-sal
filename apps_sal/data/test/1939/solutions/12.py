(n, k) = map(int, input().split())
ans = [[0] * n for i in range(n)]
q = 0
for i in range(n):
    for j in range(n):
        if j == q:
            ans[i][j] = k
    q += 1
for i in range(n):
    print(*ans[i])
