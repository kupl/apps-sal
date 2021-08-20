(n, m) = map(int, input().split())
b = [0 for i in range(200002)]
c = [0 for i in range(200002)]
hmax = 0
hmin = 200005
a = list(map(int, input().split()))
for i in range(n):
    hmax = max(hmax, a[i])
    hmin = min(hmin, a[i])
    c[a[i]] += 1
b[200000] = c[200000]
for i in range(200000 - 1, -1, -1):
    b[i] = b[i + 1] + c[i]
cur = hmax
ans = 0
while cur > hmin:
    cnt = 0
    while cnt <= m:
        if cnt + b[cur] <= m and cur > hmin:
            cnt += b[cur]
            cur -= 1
        else:
            ans += 1
            cnt = 0
            break
    if cur == hmin:
        break
print(ans)
