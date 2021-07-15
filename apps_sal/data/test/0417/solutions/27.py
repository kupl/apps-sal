INF = 10**30
def solve(n, x, d):
    if d == 0:
        if x == 0:
            return 1
        else:
            return n+1
    D = {}
    for k in range(n+1):
        l = k*x + (k-1)*k//2*d
        r = k*x + (n*k - k*(k+1)//2)*d
        c = k*x % d
        if not c in D:
            D[c] = []
        l = (l - c) // d
        r = (r - c) // d
        if l > r:
            l, r = r, l
        D[c].append((l, r))
    res = 0
    for v in D.values():
        threshold = -INF
        for l, r in sorted(v):
            l = max(l, threshold)
            res += max(0, r-l+1)
            threshold = max(threshold, r+1)
    return res

n, x, d = map(int, input().split())
print(solve(n, x, d))
