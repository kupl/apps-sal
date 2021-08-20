(n, r) = list(map(int, input().split()))
a = list(map(int, input().split()))
i = 0
d = 0
while True:
    ki = min(n - 1, i + r - 1)
    while ki >= 0 and (not a[ki]):
        ki -= 1
    if ki < 0:
        d = -1
        break
    a[ki] = 0
    d += 1
    i = ki + r
    if i > n - 1:
        break
    if i < 0:
        d = -1
        break
print(d)
