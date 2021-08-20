wejscie1 = list(map(int, input().strip().split()))
ilChlopcow = wejscie1[0]
ilRowerow = wejscie1[1]
budzet = wejscie1[2]
pieniadzeChlopcow = list(map(int, input().strip().split()))
cenyRowerow = list(map(int, input().strip().split()))
pieniadzeChlopcow = sorted(pieniadzeChlopcow)
cenyRowerow = sorted(cenyRowerow)
bikesBoysCanRent = 0
totalCostOfRenting = 0
ownMoneyRequired = 0


def czyMoznaWypozyczyc(ilSprawdzonychRowerow):
    budzet2 = budzet
    if ilSprawdzonychRowerow > ilChlopcow:
        return False
    for x in range(ilSprawdzonychRowerow):
        roznica = pieniadzeChlopcow[ilChlopcow - x - 1] - cenyRowerow[ilSprawdzonychRowerow - x - 1]
        if roznica >= 0:
            continue
        budzet2 = budzet2 + roznica
        if budzet2 < 0:
            return False
    return True


def binarySearch(lewy, prawy):
    while lewy < prawy:
        mid = (lewy + prawy + 1) // 2
        if czyMoznaWypozyczyc(mid) == True:
            lewy = mid
        else:
            prawy = mid - 1
    return lewy


bikesBoysCanRent = binarySearch(0, ilRowerow)
for x in range(bikesBoysCanRent):
    totalCostOfRenting += cenyRowerow[x]
wyjscie2 = totalCostOfRenting - budzet
if wyjscie2 < 0:
    wyjscie2 = 0
print(bikesBoysCanRent, wyjscie2)
