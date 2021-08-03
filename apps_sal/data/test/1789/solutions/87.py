n = 100
a, b, x, y = list(map(int, input().split()))
dpa = [-1] * (n + 1)
dpb = [-1] * (n + 1)
dpa[a] = 0
dpb[a] = x

for ii in range(a, n):
    dpb[ii] = dpa[ii] + x
    dpa[ii + 1] = min(dpa[ii] + y, dpb[ii] + x)

dpb[n] = min(dpa[n] + x, dpb[n - 1] + y)

for ii in range(a, 1, -1):
    dpb[ii - 1] = dpa[ii] + x
    dpa[ii - 1] = min(dpa[ii] + y, dpb[ii - 1] + x)

# print(dpa)
# print(dpb)
print((dpb[b]))
