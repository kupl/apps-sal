(n, x, v) = (int(input()), list(map(int, input().split())), list(map(int, input().split())))
(t1, t2) = (0, 10 ** 9)
while t1 + 10 ** (-6) < t2:
    t3 = (t1 + t2) / 2
    (l, r) = (1, 10 ** 9)
    for (xi, vi) in zip(x, v):
        (l, r) = (max(l, xi - vi * t3), min(r, xi + vi * t3))
    if l <= r:
        t2 = t3
    else:
        t1 = t3
print(t2)
