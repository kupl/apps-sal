import sys
sys.setrecursionlimit(100000)

N, M = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(M)]

R = {}
for a, b in AB:
    if a in R:
        R[a].append(b)
    else:
        R[a] = [b]


def nasu(x, e):
    D[x] = 1
    if x not in R:
        return []
    for i in R[x]:
        if i == e:
            return [i]
        if D[i] == 0:
            t = nasu(i, e)
            if t != []:
                return [i] + t
    return []


for i in range(1, N + 1):
    D = [0] * (N + 1)
    L = nasu(i, i)
    if L != []:
        break
else:
    print(-1)
    return

D = [0] * (N + 1)
for i in L:
    D[i] = 1

LEN = len(L)
L = L + L

i = 0
while i < LEN:
    for j in range(i + LEN - 1, i, -1):
        if D[L[j]] != 0 and L[j] in R[L[i]]:
            for k in range(j - 1, i, -1):
                D[L[k]] = 0
            i = j
            break

A = []
for i in range(LEN):
    if D[L[i]] == 1:
        A.append(L[i])

print(len(A))
for i in A:
    print(i)
