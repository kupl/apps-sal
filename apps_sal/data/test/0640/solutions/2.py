(a, b) = list(map(int, input().split()))
(pf, d, ps) = (0, 0, 0)
for i in range(1, 7):
    if abs(a - i) < abs(b - i):
        pf += 1
    elif abs(a - i) > abs(b - i):
        ps += 1
    else:
        d += 1
print(pf, d, ps)
