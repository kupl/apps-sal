(n, k, t) = list(map(int, input().split()))
if t >= k and t <= n:
    print(k)
elif t < k:
    print(t)
else:
    print(k - (t - n))
