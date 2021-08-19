(n, m) = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0
cnt = 0
a = sorted(a, key=lambda x: x[0])
for i in range(n):
    if cnt + a[i][1] < m:
        ans += a[i][0] * a[i][1]
        cnt += a[i][1]
    else:
        ans += a[i][0] * (m - cnt)
        break
print(ans)
