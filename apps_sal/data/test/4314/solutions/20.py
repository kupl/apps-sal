import numpy as np
H, W = map(int, input().split())
x = [list(map(str, list(input()))) for l in range(H)]

y = []
for i in range(H):
    if set(x[i]) != {"."}:
        y.append(x[i])

z = np.array(y)
zz = np.rot90(z)
zzz = zz.tolist()

ans = []
for i in range(W):
    if set(zzz[i]) != {"."}:
        ans.append(zzz[i])

a = np.array(ans)
b = np.rot90(a, -1)
c = b.tolist()

for i in range(len(c)):
    print(*c[i], sep='')
