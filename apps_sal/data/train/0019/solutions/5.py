t = int(input())
for u in range(t):
    (n, d, k) = map(int, input().split())
    a = list(map(int, input().split()))
    c = set()
    b = {}
    ans = 10 ** 9
    for i in range(min(n, k)):
        c.add(a[i])
        if a[i] in b:
            b[a[i]] += 1
        else:
            b[a[i]] = 1
    i = k
    ans = min(ans, len(c))
    while i < n:
        b[a[i - k]] -= 1
        if b[a[i - k]] == 0:
            c.discard(a[i - k])
        if a[i] in b:
            b[a[i]] += 1
        else:
            b[a[i]] = 1
        c.add(a[i])
        ans = min(ans, len(c))
        i += 1
    print(ans)
