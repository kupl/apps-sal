N = int(input())
E = []
for i in range(N - 1):
    E.append(list(map(int, input().split())))
V = []
for i in range(N):
    V.append([])
for e in E:
    if e[0] > e[1]:
        V[e[0] - 1].append(e[1] - 1)
    else:
        V[e[1] - 1].append(e[0] - 1)
S = 0
F = 0
for i in range(N):
    F = F + i + 1 - sum([j + 1 for j in V[i]])
    S += F
print(S)
