(n, k, t) = map(int, input().split())
if t <= k:
    print(t)
elif t >= n:
    print(n + k - t)
else:
    print(k)
