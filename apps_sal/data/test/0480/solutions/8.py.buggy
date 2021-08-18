s, x1, x2 = list(map(int, input().split()))
t1, t2 = list(map(int, input().split()))
p, d = list(map(int, input().split()))

if x2 < x1:
    x1, x2 = s - x1, s - x2
    d *= -1
    p = s - p


if t2 <= t1:
    print(t2 * abs(x1 - x2))
    return

if p <= x1 and d == 1:
    print(min(t2 * abs(x1 - x2), t1 * abs(p - x2)))
elif d == 1:
    print(min(t2 * abs(x1 - x2), t1 * s + t1 * (s - p) + t1 * abs(x2)))
else:
    print(min(t2 * abs(x1 - x2), t1 * (p) + t1 * abs(x2)))
