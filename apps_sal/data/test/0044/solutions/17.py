(d, k, a, b, t) = [int(i) for i in input().split()]
if k >= d:
    print(a * d)
elif a * k + t >= b * k:
    print(a * k + b * (d - k))
elif d % k == 0:
    print((d // k - 1) * t + a * d)
else:
    print(min(d // k * t + a * d, (d // k - 1) * t + (d - d % k) * a + d % k * b))
