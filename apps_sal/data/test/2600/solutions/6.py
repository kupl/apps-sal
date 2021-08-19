t = int(input())
for _ in range(t):
    (n, m) = list(map(int, input().split()))
    a = [list(map(int, input().split())) for _ in range(n)]
    k = [0] * (n + m - 1)
    c = [0] * (n + m - 1)
    for i in range(n):
        for j in range(m):
            c[i + j] += 1
            if a[i][j] == 1:
                k[i + j] += 1
    ans = 0
    for i in range((n + m - 1) // 2):
        j = n + m - 2 - i
        ans += min(k[i] + k[j], c[i] + c[j] - k[i] - k[j])
    print(ans)
