n, m = list(map(int, input().split()))
d = [set() for q in range(n)]
for q in range(m):
    l, r = list(map(int, input().split()))
    l, r = l - 1, r - 1
    d[l].add(r)
    d[r].add(l)
ans = -1
for q in range(n):
    if len(d[q]) < n - 1:
        ans = q
        break
if ans == -1:
    print('NO')
else:
    for q in range(n):
        if q != ans and q not in d[ans]:
            ans = [ans, q]
            break
    ans, ans1 = min(ans), max(ans)
    a = []
    s = []
    for q in range(ans + 1):
        a.append(1 + q)
        s.append(1 + q)
    for q in range(ans + 1, ans1):
        a.append(2 + q)
        s.append(2 + q)
    a.append(ans + 1)
    s.append(ans + 2)
    for q in range(ans1 + 1, n):
        a.append(1 + q)
        s.append(1 + q)
    print('YES')
    print(*s)
    print(*a)
