T = input().split(' ')
n = int(T[0])
m = int(T[1])
L = [0] * n
M = []
D = [0] * m
F = [0] * m
for i in range(m):
    S = input().split(' ')
    a = int(S[0])
    b = int(S[1])
    c = int(S[2])
    L[b-1] = m+1
    F[i] = b-1
    M.append((a-1, b-2, i+1))
    D[i] = c
M.sort()
for i in range(n):
    if L[i] == 0:
        G = []
        for j in range(len(M)):
            if M[j][0]<=i:
                G.append((M[j][1], M[j][2]))
        G.sort()
        for k in range(len(G)):
            if D[G[k][1]-1] > 0 and F[G[k][1]-1]>i:
                D[G[k][1]-1]-=1
                L[i] = G[k][1]
                break
b = True
for j in range(len(D)):
    if D[j] > 0:
        b = False
if b:
    for i in range(n-1):
        print(L[i], end=' ')
    print(L[n-1])
else:
    print(-1)

