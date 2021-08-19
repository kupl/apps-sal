(d, k, a, b, t) = map(int, input().split())
if d <= k:
    print(a * d)
elif a * k + t > k * b:
    print(a * k + (d - k) * b)
else:
    s = d % k
    x = d // k
    if x >= 1:
        im = a * k * x + t * (x - 1)
    else:
        im = 0
    aaa = t + a * s
    bbb = s * b
    im += min(aaa, bbb)
    print(im)
