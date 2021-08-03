n, h = list(map(int, input().split()))
l = list(map(int, input().split()))


def poss(k):
    tab = sorted(l[:k])
    suma = 0
    i = k - 1
    while i >= 0:
        suma += tab[i]
        i -= 2
    if suma > h:
        return False
    return True


lo = 0
hi = n
kand = 0
while True:
    if (poss((lo + hi) // 2)):
        lo = ((lo + hi) // 2)
    else:
        hi = ((lo + hi) // 2)
    if abs(lo - hi) < 2:
        kand = lo
        break
if poss(kand + 1):
    print(kand + 1)
else:
    print(kand)
