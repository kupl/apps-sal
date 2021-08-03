from collections import Counter
def R(): return map(int, input().split())


n = int(input())
v = list(R())
mn = min(v)
mx = max(v)
c = Counter(v)

if mn == mx or mn == mx - 1:
    print(len(v))
    print(" ".join(map(str, v)))
    return

if mn == mx - 2 and len(c) == 2:
    c[mn + 1] = 0

k = sorted(list(c.keys()))
ck0 = c[k[0]]
ck1 = c[k[1]]
ck2 = c[k[2]]
if (2 * min(ck0, ck2) <= 2 * (ck1 // 2)):
    i = [i for i in range(len(v)) if v[i] == k[1]]
    for j in range(ck1 // 2):
        v[i[2 * j]], v[i[2 * j + 1]] = v[i[2 * j]] - 1, v[i[2 * j + 1]] + 1
    print(len(v) - 2 * (ck1 // 2))
    print(" ".join(map(str, v)))
else:
    mni = [i for i in range(len(v)) if v[i] == mn]
    mxi = [i for i in range(len(v)) if v[i] == mx]
    for i in range(min(ck0, ck2)):
        v[mni[i]], v[mxi[i]] = v[mni[i]] + 1, v[mxi[i]] - 1
    print(len(v) - 2 * (min(ck0, ck2)))
    print(" ".join(map(str, v)))
