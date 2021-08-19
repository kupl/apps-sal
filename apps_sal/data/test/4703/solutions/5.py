import itertools
S = input()
npm = len(S) - 1
sum = eval(S)
pcomb = []
for i in range(npm):
    pcomb.append(list(itertools.combinations(list(range(1, npm + 1)), i + 1)))
for j in pcomb:
    k = 0
    for l in range(len(j)):
        pcomb2 = j[k]
        npmc = 0
        F = S
        for m in pcomb2:
            F = F[:m + npmc] + '+' + F[m + npmc:]
            npmc += 1
        sum += eval(F)
        k += 1
print(sum)
