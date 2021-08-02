n, m = list(map(int, input().split()))
c = [[0] * n for i in range(n)]
for i in range(m):
    a, b = list(map(int, input().split()))
    c[a - 1][b - 1] = 1
    c[b - 1][a - 1] = 1
ans = 0
for k in range(n):
    for i in range(n):
        if sum(c[i]) == 1:
            ans += 1
            for j in range(n):
                if c[i][j] == 1:
                    c[i][j] = 0
                    c[j][i] = 0
print(ans)
