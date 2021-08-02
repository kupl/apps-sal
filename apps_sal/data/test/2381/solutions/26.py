MOD = 10 ** 9 + 7

n, k = map(int, input().split())
a = list(map(int, input().split()))
aplus, aminus = [], []

for i in range(n):
    if a[i] >= 0: aplus.append(a[i])
    else: aminus.append(a[i])


if len(aplus) == 0 and k % 2 == 1:
    asort = sorted(a, reverse=True)
    ans = 1
    for i in range(k):
        ans = (ans * asort[i]) % MOD
    print(ans)
    return

if n == k:
    ans = 1
    for i in range(k):
        ans = (ans * a[i]) % MOD
    print(ans)
    return

newa = sorted(a, reverse=True, key=abs)
newaplus = sorted(aplus, reverse=True)
newaminus = sorted(aminus)

cntp, cntm, pp, mm = 0, 0, 0, 0

for i in range(k):
    if newa[i] >= 0:
        cntp += 1
        pp = i
    else:
        cntm += 1
        mm = i

if cntm % 2 == 1:
    if cntp == 0:
        newa[mm] = newaplus[cntp]
    elif len(newaplus) == cntp:
        newa[pp] = newaminus[cntm]
    elif len(newaminus) == cntm:
        newa[mm] = newaplus[cntp]
    else:
        if newa[pp] * newaplus[cntp] >= newa[mm] * newaminus[cntm]:
            newa[mm] = newaplus[cntp]
        else:
            newa[pp] = newaminus[cntm]

ans = 1
for i in range(k):
    ans = (ans * newa[i]) % MOD

print(ans)
