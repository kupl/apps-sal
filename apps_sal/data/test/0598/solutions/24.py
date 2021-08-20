def f():
    return list(map(int, input().split()))


(n, x) = f()
s = [[] for i in range(x - 1)]
for d in range(n):
    (l, r, c) = f()
    if r - l < x - 1:
        s[r - l].append((l, c))
for t in s:
    t.sort(key=lambda q: q[0])
m = 3000000000.0
for (d, t) in enumerate(s):
    D = x - 2 - d
    (i, T) = (0, s[D])
    M = 3000000000.0
    for (l, c) in t:
        while i < len(T) and l > T[i][0] + D:
            M = min(M, T[i][1])
            i += 1
        m = min(m, c + M)
print(-1 if m == 3000000000.0 else m)
