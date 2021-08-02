n, k = map(int, input().split())
ans = 0
if k == 0:
    print(n * n)
else:
    g = 0
    for b in range(k + 1, n + 1):
        t = n // b
        g += t * (b - k)
        if t * b + k <= n < (t + 1) * b:
            g += n - (t * b + k) + 1
    print(g)
