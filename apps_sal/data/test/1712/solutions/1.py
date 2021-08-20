__author__ = 'PrimuS'
(n, a, b) = (int(x) for x in input().split())
mobs = [0] * n
for i in range(n):
    mobs[i] = int(input())
total = a + b
ans = [0] * (total + 1)
aa = 0
bb = 0
ans[0] = 2
i = 1
while i <= total:
    t1 = aa + b
    t2 = bb + a
    if t1 == t2:
        aa += b
        bb += a
        ans[i] = 2
        ans[i + 1] = 2
        i += 2
    elif t1 < t2:
        aa = t1
        ans[i] = 0
        i += 1
    else:
        bb = t2
        ans[i] = 1
        i += 1
res = [''] * len(mobs)
i = 0
for m in mobs:
    k = m % total
    if ans[k] == 0:
        res[i] = 'Vanya'
    elif ans[k] == 1:
        res[i] = 'Vova'
    else:
        res[i] = 'Both'
    i += 1
print('\n'.join(res))
