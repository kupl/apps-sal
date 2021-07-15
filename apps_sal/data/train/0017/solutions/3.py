t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    d = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] == a[j]:
                d[i][j] = 1
    for i in range(n):
        for j in range(n - 1):
            d[i][j + 1] += d[i][j]
    for i in range(n - 1):
        for j in range(n):
            d[i + 1][j] += d[i][j]
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] == a[j]:
                ans += d[j - 1][n - 1] - d[j - 1][j] - d[i][n - 1] + d[i][j]
    print(ans)
