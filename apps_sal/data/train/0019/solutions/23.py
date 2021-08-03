t = int(input())
for q in range(t):
    n, k, d = list(map(int, input().split()))
    a = list(map(int, input().split()))
    g = {}
    m = k
    j = 0
    s = 0
    for i in range(0, n):
        f = a[i]
        l = g.get(f, 0)
        g[f] = l + 1
        j += 1
        if l == 0:
            s += 1
        if j > d:
            vr = g[a[i - d]]
            g[a[i - d]] -= 1
            j -= 1
            if vr == 1:
                s -= 1
        if j == d:
            m = min(m, s)
    print(m)
