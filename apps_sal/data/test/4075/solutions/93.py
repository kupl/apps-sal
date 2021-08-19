(n, m) = map(int, input().split())
li = []
for i in range(m):
    a = list(map(int, input().split()))
    li.append(a[1:])
p = list(map(int, input().split()))
ans = 0
for i in range(1 << n):
    ok = 1
    s = []
    for j in range(n):
        if i >> j & 1:
            s.append(j)
    for j in range(m):
        tmp = 0
        for k in li[j]:
            if k - 1 in s:
                tmp += 1
        if tmp % 2 != p[j]:
            ok = 0
    if ok:
        ans += 1
print(ans)
