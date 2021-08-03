def f(): return map(int, input().split())


n, m = f()
s = [0] * n
for i in range(m):
    t, k, d = f()
    j, p = 0, []
    while j < n and len(p) < k:
        if s[j] <= t:
            p.append(j)
        j += 1
    if len(p) < k:
        print(-1)
    else:
        for j in p:
            s[j] = t + d
        print(sum(p) + k)
