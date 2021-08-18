d, k, a, b, t = list(map(int, input().split()))


if a >= b:
    print(b * d)
elif k >= d:
    print(a * d)

elif a * k + t <= b * k:
    interval = d // k
    if d % k == 0:
        interval -= 1
    print(min(a * d + interval * t, a * (d - (d % k)) + ((d // k) - 1) * t + (d % k) * b))
else:
    print(k * a + (d - k) * b)
