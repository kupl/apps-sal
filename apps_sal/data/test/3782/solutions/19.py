n, k, q = map(int, input().split())
a = list(map(int, input().split()))
ans = 10**10
for x in a:
    b = [[]]
    can = 0
    for i in a:
        if i < x:
            if len(b[-1]): b.append([])
        else: b[-1].append(i)
    if len(b[-1]) == 0: del b[-1]
    for i in range(len(b)): b[i].sort()
    c = []
    for i in b:
        i.sort()
        if len(i) >= k: c += i[:len(i) - k + 1]
    if len(c) < q: continue
    c.sort()
    ans = min(ans, c[q - 1] - c[0])
print(ans)
