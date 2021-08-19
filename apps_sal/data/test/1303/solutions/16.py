(p, q, l, r) = map(int, input().split())
t = [0] * 1002
z = [list(map(int, input().split())) for i in range(p)]
x = [list(map(int, input().split())) for i in range(q)]
for (xl, xr) in x:
    for (zl, zr) in z:
        (a, b) = (zl - xr, zr - xl + 1)
        if b <= l:
            continue
        if a > r:
            break
        if a < l:
            a = l - 1
        if b <= r:
            t[b] -= 1
        t[a] += 1
for i in range(l, r + 1):
    t[i] += t[i - 1]
print(r - l + 1 - t[l:r + 1].count(0))
