N = int(input())
L = [list(map(int, input().split())) for i in range(N)]
zmax = zmin = L[0][0] + L[0][1]
wmax = wmin = L[0][0] - L[0][1]
for a, b in L:
    z, w = a + b, a - b
    zmax = max(zmax, z)
    zmin = min(zmin, z)
    wmax = max(wmax, w)
    wmin = min(wmin, w)
print(max(zmax - zmin, wmax - wmin))
