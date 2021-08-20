def getTableKMP(Ss):
    Ss += '$'
    lenS = len(Ss)
    table = [-1] * lenS
    j = -1
    for i in range(lenS - 1):
        while j >= 0 and Ss[i] != Ss[j]:
            j = table[j]
        j += 1
        if Ss[i + 1] == Ss[j]:
            table[i + 1] = table[j]
        else:
            table[i + 1] = j
    return table


def getPosPtnsKMP(Ss, ptn, table):
    anss = []
    (lenS, lenP) = (len(Ss), len(ptn))
    (iS, iP) = (0, 0)
    while iS < lenS:
        if Ss[iS] == ptn[iP]:
            iS += 1
            iP += 1
            if iP == lenP:
                anss.append(iS - lenP)
                iP = table[iP]
        else:
            iP = table[iP]
            if iP == -1:
                iS += 1
                iP = 0
    return anss


Ss = input()
Ts = input()
(lenS, lenT) = (len(Ss), len(Ts))
num = (lenT + lenS - 1 + lenS - 1) // lenS
S2s = Ss * num
tableKMP = getTableKMP(Ts)
posPtns = getPosPtnsKMP(S2s, Ts, tableKMP)
isFounds = [False] * lenS
for pos in posPtns:
    if pos >= lenS:
        break
    isFounds[pos] = True
ans = 0
numDone = 0
for i in range(lenS):
    if not isFounds[i]:
        i = (i + lenT) % lenS
        for num in range(lenS + 1):
            if not isFounds[i]:
                ans = max(ans, num)
                numDone += num + 1
                break
            i = (i + lenT) % lenS
        else:
            ans = -1
            break
if numDone < lenS:
    ans = -1
print(ans)
