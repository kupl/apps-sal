import math

to_min = lambda h, m: h * 60 + m

hh, mm = list(map(int, input().split()))
h, d, c, n = list(map(int, input().split()))

t = to_min(hh, mm)
dt = to_min(20, 0)

if t < dt:
    dh = ((dt - t) * d) + h
    dp = math.ceil(dh/n)
    p = math.ceil(h/n)
    print(min(0.8*dp*c, p*c))
else:
    print(0.8*c*math.ceil(h/n))

