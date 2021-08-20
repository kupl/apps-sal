def factor(n):
    rtn = []
    p = 2
    tmp = n
    while p * p <= tmp:
        q = 0
        while tmp % p == 0:
            tmp //= p
            q += 1
        if 0 < q:
            rtn.append((p, q))
        p += 1
    if 1 < tmp:
        rtn.append((tmp, 1))
    return rtn


def divs(n):
    rtn = [1]
    arr = factor(n)
    for (p, q) in arr:
        ds = [p ** i for i in range(1, q + 1)]
        tmp = rtn[:]
        for d in ds:
            for t in tmp:
                rtn.append(d * t)
    return list(sorted(rtn))


(n, k) = list(map(int, input().split()))
ds = divs(n)
l = 0
r = len(ds) - 1
while l + 1 < r:
    c = (l + r) // 2
    if ds[c] * k * (k + 1) // 2 <= n:
        l = c
    else:
        r = c
if l == 0 and n < k * (k + 1) // 2:
    print(-1)
else:
    d = ds[l]
    ans = [d * (i + 1) for i in range(k)]
    ans[-1] += n - sum(ans)
    print(' '.join(map(str, ans)))
