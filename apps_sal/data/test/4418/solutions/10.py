import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

B = []
C = []
D = []
E = []
F = []
G = []

for i in range(n):
    if A[i] == 4:
        B.append(i)

    if A[i] == 8:
        C.append(i)

    if A[i] == 15:
        D.append(i)

    if A[i] == 16:
        E.append(i)

    if A[i] == 23:
        F.append(i)

    if A[i] == 42:
        G.append(i)

NOW = 0
Bi = 0
Ci = 0
Di = 0
Ei = 0
Fi = 0
Gi = 0

ANS = 0

while True:

    for b in range(Bi, len(B)):
        NOW = B[b]
        Bi = b + 1
        break
    else:
        break

    # print("!")

    for c in range(Ci, len(C)):
        if C[c] >= NOW:
            NOW = C[c]
            Ci = c + 1
            break
    else:
        break

    for d in range(Di, len(D)):
        if D[d] >= NOW:
            NOW = D[d]
            Di = d + 1
            break
    else:
        break

    for e in range(Ei, len(E)):
        if E[e] >= NOW:
            NOW = E[e]
            Ei = e + 1
            break
    else:
        break

    for f in range(Fi, len(F)):
        if F[f] >= NOW:
            NOW = F[f]
            Fi = f + 1
            break
    else:
        break

    for g in range(Gi, len(G)):
        if G[g] >= NOW:
            NOW = G[g]
            Gi = g + 1
            break
    else:
        break

    ANS += 6

print(len(A) - ANS)
