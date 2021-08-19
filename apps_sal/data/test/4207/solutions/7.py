import math
n = int(input())
x = [*map(int, input().split())]
y = [*map(int, input().split())]
cnt = dict()
fixcnt = 0
zeroToCnt = 0
for i in range(n):
    if x[i] == 0:
        if y[i] == 0:
            fixcnt += 1
        continue
    if y[i] == 0:
        zeroToCnt += 1
        continue
    gc = math.gcd(x[i], y[i])
    (tx, ty) = (x[i] // gc, y[i] // gc)
    if tx * ty >= 0:
        si = True
    else:
        si = False
    cnt[abs(tx), abs(ty), si] = cnt.get((abs(tx), abs(ty), si), 0) + 1
cntRes = max(zeroToCnt, max(cnt.values() if cnt else [0]))
print(cntRes + fixcnt)
