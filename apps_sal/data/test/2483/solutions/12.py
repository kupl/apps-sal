N, C = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
D = [[] for i in range(C)]
DD = [[] for i in range(C)]
for s, t, c in A:
    D[c - 1].append([s, t])
for i in range(C):
    E = sorted(D[i])
    e = len(E)
    for j in range(e):
        if j == 0:
            DD[i].append([E[j][0], E[j][1]])
        elif j != 0 and E[j][0] == E[j - 1][1]:
            DD[i][-1][-1] = E[j][1]
        else:
            DD[i].append([E[j][0], E[j][1]])
ANS = [0] * (10**5 + 3)
for i in range(C):
    F = DD[i]
    for i, j in F:
        ANS[i] += 1
        ANS[j + 1] -= 1
ans = 0
d = 0
for i in ANS:
    d += i
    ans = max(d, ans)
print(ans)
