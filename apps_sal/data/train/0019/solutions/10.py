t = int(input())
for _ in range(t):
    (n, k, d) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    m = dict()
    for i in range(d):
        if a[i] not in m:
            m[a[i]] = 0
        m[a[i]] += 1
    ans = len(m)
    for i in range(n - d):
        m[a[i]] -= 1
        if m[a[i]] == 0:
            m.pop(a[i])
        if a[i + d] not in m:
            m[a[i + d]] = 0
        m[a[i + d]] += 1
        ans = min(ans, len(m))
    print(ans)
