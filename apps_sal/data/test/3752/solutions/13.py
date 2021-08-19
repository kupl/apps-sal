(k, d, t) = list(map(int, input().split()))
t *= 2
days = 0
if k == d:
    days = t / 2
elif k > d:
    p = t // (2 * k + d - (k - 1) % d - 1)
    days += p * (k + d - (k - 1) % d - 1)
    t = t % (2 * k + d - (k - 1) % d - 1)
    if t < 2 * k:
        days += t / 2
    else:
        days += k
        t -= 2 * k
        days += t
else:
    p = t // (d + k)
    days += p * d
    t = t % (d + k)
    if t < 2 * k:
        days += t / 2
    else:
        days += k
        t -= 2 * k
        days += t
print(days)
