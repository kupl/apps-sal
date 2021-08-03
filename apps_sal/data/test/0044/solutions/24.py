d, k, a, b, t = list(map(int, input().split()))
T = 0
if k >= d:
    print(d * a)
    return
if (t + a * k) >= b * k:
    print(k * a + b * (d - k))
    return
else:
    if (d % k) * a + t < b * (d % k):
        T = (d // k) * k * a + (d % k) * a + t * (d // k)
    else:
        T = (d // k) * k * a + b * (d % k) + t * (d // k - 1)
    print(T)
