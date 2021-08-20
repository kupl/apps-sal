M = 4 * 10 ** 9 + 1
n = int(input().strip())


def f(t):
    return (int(t[0]), t[1])


xcis = [(-M, 'P')] + [f(input().strip().split()) for _ in range(n)] + [(M, 'P')]
iPs = [i for i in range(len(xcis)) if xcis[i][1] == 'P']
iRs = [i for i in range(len(xcis)) if xcis[i][1] == 'R']
iBs = [i for i in range(len(xcis)) if xcis[i][1] == 'B']
l = 0
for iiP in range(1, len(iPs)):
    iP0 = iPs[iiP - 1]
    iP1 = iPs[iiP]
    dRmax = 0
    dBmax = 0
    (xR, _) = xcis[iP0]
    (xB, _) = xcis[iP0]
    for i in range(iP0 + 1, iP1 + 1):
        (x, c) = xcis[i]
        if c in 'RP':
            dRmax = max(dRmax, x - xR)
            xR = x
        if c in 'BP':
            dBmax = max(dBmax, x - xB)
            xB = x
    d = xcis[iP1][0] - xcis[iP0][0]
    l += d + min(d, 2 * d - dBmax - dRmax)
    if iiP in [1, len(iPs) - 1]:
        l -= d
    iP0 = iP1
if len(iPs) == 2:
    l = 0 if len(iRs) < 2 else xcis[iRs[-1]][0] - xcis[iRs[0]][0]
    l += 0 if len(iBs) < 2 else xcis[iBs[-1]][0] - xcis[iBs[0]][0]
print(l)
