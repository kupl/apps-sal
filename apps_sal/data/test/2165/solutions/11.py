def R():
    return list(map(int, input().split()))


(n, t) = R()
a = R()
b = R()
x = [[t - b[i], a[i]] for i in range(n)]
x.sort()
(c, v) = (sum(a), sum((i * j for (i, j) in x)))
if v:
    f = 2 * (v < 0) - 1
    for i in range(n)[::f]:
        if f * (v - x[i][1] * x[i][0]) >= 0:
            c -= v / x[i][0]
            break
        c -= x[i][1]
        v -= x[i][0] * x[i][1]
print(c)
