(n, m, x) = list(map(int, input().split()))
ca = [list(map(int, input().split())) for _ in range(n)]
sum = 0
for i in range(n):
    sum += ca[i][0]
ans = sum + 1
for i in range(2 ** n):
    cnt = 0
    a = [0] * m
    for j in range(n):
        if i >> j & 1:
            for k in range(m):
                a[k] += ca[j][k + 1]
            cnt += ca[j][0]
    if cnt > 0 and min(a) >= x:
        ans = min(cnt, ans)
if ans == sum + 1:
    print(-1)
else:
    print(ans)
