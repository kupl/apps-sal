(n, k, t) = map(int, input().split())
if t <= n:
    print(min(t, k))
else:
    print(k - t + n)
