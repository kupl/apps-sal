(n, t) = map(int, input().split())
a = list(map(int, input().split()))
x = min(a)
cands = 0
while t >= x:
    y = sum(a)
    if t >= y:
        f = len(a)
        cands += t // y * f
        t = t - t // y * y
    else:
        for item in a:
            if t >= item:
                t = t - item
                cands += 1
    a = [_ for _ in a if _ <= t]
print(cands)
