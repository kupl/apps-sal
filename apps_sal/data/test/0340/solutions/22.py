n = int(input())
fac = {}
nn = n
maxe = 1
while nn % 2 == 0:
    fac[2] = fac.get(2, 0) + 1
    nn >>= 1
for i in range(3, nn + 1, 2):
    if i * i > nn:
        break
    while nn % i == 0:
        fac[i] = fac.get(i, 0) + 1
        nn //= i
if nn > 1:
    fac[nn] = 1
maxe = 1
mine = n
prod = 1
for f in fac:
    if fac[f] > maxe:
        maxe = fac[f]
    if fac[f] < mine:
        mine = fac[f]
    prod *= f
ops = 0
t = 1
while t < maxe:
    t <<= 1
    ops += 1
if mine < t:
    ops += 1
print(prod, ops)
