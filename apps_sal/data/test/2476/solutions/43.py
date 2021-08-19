from collections import Counter
N = int(input())
As = list(map(int, input().split()))
cntA = Counter(As)
cntCntA = Counter(list(cntA.values()))
accDs = [cntCntA[0]]
for i in range(1, N + 1):
    accDs.append(accDs[-1] + cntCntA[i])
accKDs = [0]
for i in range(1, N + 1):
    accKDs.append(accKDs[-1] + i * cntCntA[i])
fXs = [0]
for X in range(1, N + 1):
    fXs.append((accKDs[X] + X * (accDs[N] - accDs[X])) // X)
anss = [0] * (N + 1)
for (X, fX) in enumerate(fXs):
    anss[fX] = X
for i in reversed(list(range(N))):
    if anss[i] == 0:
        anss[i] = anss[i + 1]
print('\n'.join(map(str, anss[1:])))
