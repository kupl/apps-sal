n, k = [int(a) for a in input().split()]

field = []
for i in range(n):
    field.append(input())

poss = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n - k + 1):
        good = True
        for ell in range(k):
            if field[j + ell][i] == '#':
                good = False
        if good:
            for ell in range(k):
                poss[j + ell][i] += 1

        good = True
        for ell in range(k):
            if field[i][j + ell] == '#':
                good = False
        if good:
            for ell in range(k):
                poss[i][j + ell] += 1

best = 0
besti = 0
bestj = 0
for i in range(n):
    for j in range(n):
        if best < poss[i][j]:
            best = poss[i][j]
            besti = i
            bestj = j

print(besti + 1, bestj + 1)
