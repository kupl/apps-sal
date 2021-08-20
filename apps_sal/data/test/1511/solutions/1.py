(n, m, k) = list(map(int, input().split()))
L = []
for i in range(n):
    L.append(list(map(int, input().split())))
Locked = [-1] * n
Z = {}
for i in range(m):
    K = {}
    for j in range(n):
        if Locked[j] != -1:
            continue
        if L[j][i] in K:
            K[L[j][i]].append(j)
        else:
            K[L[j][i]] = [j]
    for item in K:
        if item == 0:
            continue
        if item in Z:
            for e in K[item]:
                if Locked[e] == -1:
                    Locked[e] = i
        elif len(K[item]) > 1:
            Z[item] = 1
            for e in K[item]:
                if Locked[e] == -1:
                    Locked[e] = i
for i in range(n):
    print(Locked[i] + 1)
