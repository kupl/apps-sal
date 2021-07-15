n, m, c = map(int, input().split())
b = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    s = 0
    for j in range(m):
        s += a[i][j] * b[j]
    if s + c > 0:
        ans += 1
print(ans)
