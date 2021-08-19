t = int(input())
for _ in range(t):
    (n, m) = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n // 2):
        for j in range(m // 2):
            s = [a[i][j], a[n - i - 1][j], a[i][m - j - 1], a[n - i - 1][m - j - 1]]
            s.sort()
            for t in s:
                ans += abs(t - s[1])
    if n % 2 == 1:
        for i in range(m // 2):
            ans += abs(a[n // 2][i] - a[n // 2][m - i - 1])
    if m % 2 == 1:
        for i in range(n // 2):
            ans += abs(a[i][m // 2] - a[n - i - 1][m // 2])
    print(ans)
