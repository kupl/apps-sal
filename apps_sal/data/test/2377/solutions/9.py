(n, h) = list(map(int, input().split()))
wield = 0
bs = []
for i in range(n):
    (a, b) = list(map(int, input().split()))
    if a > wield:
        wield = a
    bs.append(b)
throw = []
for i in range(n):
    if bs[i] > wield:
        throw.append(bs[i])
total = sum(throw)
if total > h:
    throw = sorted(throw, reverse=True)
    total = 0
    ind = 0
    while total < h:
        total += throw[ind]
        ind += 1
    print(ind)
else:
    print((h - total + wield - 1) // wield + len(throw))
