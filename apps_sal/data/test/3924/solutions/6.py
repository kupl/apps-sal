(n, k) = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
p = 0
cp = 0
sdg = 0
fdg = 0
tg = 0
fplp = 0
for d in range(n - 1):
    fdg = a[d]
    cp = sdg // k + (0 if sdg % k == 0 else 1)
    fplp = k - sdg % k
    if fplp == k:
        fplp = 0
    fdg -= min(fplp, fdg)
    cp += fdg // k
    fdg -= fdg // k * k
    p += cp
    sdg = fdg
fdg = a[n - 1]
p += (sdg + fdg) // k + (0 if (sdg + fdg) % k == 0 else 1)
print(p)
