import math
d, G = map(int, input().split())
g = G // 100
plist = [list() for _ in range(d)]
pp = []
pe = []
for i in range(d):
    p, C = map(int, input().split())
    c = C // 100
    pp += [p]
    if p == 1:
        pe += [i]
    plist[i] += [i + 1] * (p - 1)
    plist[i] += [i + 1 + c]

poli = [list() for _ in range(d)]
for i in range(d):
    poli[i] += [plist[i][0]]
    for j in range(pp[i] - 1):
        poli[i] += [poli[i][j] + plist[i][j + 1]]

numli = []
for i in range(2**d):
    kari = 0
    nkanli = []
    karimon = 0
    for j in range(d):
        if (i >> j) & 1 == 1:
            kari += poli[j][-1]
            karimon += pp[j]
        else:
            nkanli += [j]
    if kari >= g:
        numli += [karimon]
    else:
        if nkanli == []:
            continue
        else:
            for k in range(len(nkanli) - 1, -1, -1):
                if nkanli[k] in pe:
                    continue
                else:
                    if kari + poli[nkanli[k]][-2] >= g:
                        karimon += math.ceil((g - kari) / (nkanli[k] + 1))
                        numli += [karimon]
                        break
                    else:
                        break
    # print(kari,nkanli,karimon)
# print(numli)
print(min(numli))
