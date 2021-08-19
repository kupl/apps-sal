N = int(input())
D = {}
for i in range(N):
    T = [x for x in input().split()]
    if T[i] == 'T':
        L = []
        for j in range(N):
            if T[j] == 'T':
                L.append(j)
        x = tuple(L)
        if x in D:
            D[x] += 1
        else:
            D[x] = 1
best = 0
for i in D:
    if len(i) == D[i]:
        best = max(best, D[i])
print(best)
