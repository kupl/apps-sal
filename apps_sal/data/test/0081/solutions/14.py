(are, bre) = list(map(int, input().split()))


def plottt(xre, yre):
    if xre == 0:
        return yre
    if yre == 0:
        return xre
    if yre > xre:
        (yre, xre) = (xre, yre)
    return plottt(xre % yre, yre)


if are > bre:
    (are, bre) = (bre, are)
kre = bre - are
plkiyer = []
ire = 1
while ire ** 2 <= kre:
    if kre % ire == 0:
        plkiyer.append(ire)
        plkiyer.append(kre // ire)
    ire += 1
plotttd = are * bre / plottt(are, bre)
result = 0
for dre in plkiyer:
    aare = are - are % dre + dre
    bbre = bre - bre % dre + dre
    if aare * bbre // plottt(aare, bbre) <= plotttd:
        if aare * bbre // plottt(aare, bbre) == plotttd:
            result = min(dre - are % dre, result)
        else:
            plotttd = aare * bbre // plottt(aare, bbre)
            result = dre - are % dre
print(result)
