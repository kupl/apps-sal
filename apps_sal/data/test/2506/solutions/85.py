n, m = map(int, input().split())
a = sorted(list(map(int, input().split())), reverse=True)
a_rev = a[::-1]

ok, ng = 1, 200001
while ng - ok > 1:
    x = (ok + ng) // 2
    num = 0
    cur = 0
    for i in range(n - 1, -1, -1):
        while cur < n and a[i] + a[cur] >= x:
            cur += 1
        num += cur
    if num < m:
        ng = x
    else:
        ok = x
just = ok

ans = 0
larger_cnt = 0
cur = 0

a_cum = [0]
for i in range(n):
    a_cum.append(a_cum[-1] + a[i])

for i in range(n):
    while cur < n and a[i] + a_rev[cur] <= just:
        cur += 1
    larger_cnt += n - cur
    ans += (n - cur) * a[i] + a_cum[n - cur]

ans += just * (m - larger_cnt)
print(ans)
