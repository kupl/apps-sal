N, K, Q, *A = map(int, open(0).read().split())
ans = 10**10
for i in range(N - K + 1):
    c = min(A[i:i + K])
    ls = []
    x = []
    for d in A:
        if d >= c:
            x.append(d)
        else:
            ls.append(x)
            x = []
    ls.append(x)
    m = []
    for x in ls:
        x.sort()
        m += x[:max(len(x) - K + 1, 0)]
    if len(m) < Q:
        continue
    m.sort()
    y = m[Q - 1]
    ans = min(ans, y - c)
print(ans)
