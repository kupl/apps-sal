from itertools import product
N, M = list(map(int, input().split()))
Switch = [list([int(a) - 1 for a in input().split()])[1:] for i in range(M)]
P = list(map(int, input().split()))

Target = product([0, 1], repeat=N)
ans = 0
for T in Target:
    akari = []
    for i, S in enumerate(Switch):
        temp = 0
        for s in S:
            a = T[s]
            if a == 1:
                temp += 1
        akari.append(temp)
    isOK = True
    for j, ak in enumerate(akari):
        if ak % 2 != P[j]: isOK = False
    if isOK:
        ans += 1
print(ans)
