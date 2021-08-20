(n, d) = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        ans = 0
        for k in range(d):
            ans += (x[i][k] - x[j][k]) ** 2
        ans = ans ** (1 / 2)
        if ans % 1 == 0:
            cnt += 1
print(cnt)
