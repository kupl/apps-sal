import copy
(n, h, l, r) = map(int, input().split())
A = list(map(int, input().split()))
V = [0] * h
V[0] = 1
G = [0] * h
for i in range(n):
    R = [0] * h
    RG = [0] * h
    for j in range(h):
        if V[j] == 1:
            X = (j + A[i]) % h
            Y = (j + A[i] + h - 1) % h
            R[X] = R[Y] = 1
            if l <= X <= r:
                RG[X] = max(RG[X], 1 + G[j])
            else:
                RG[X] = max(RG[X], G[j])
            if l <= Y <= r:
                RG[Y] = max(RG[Y], 1 + G[j])
            else:
                RG[Y] = max(RG[Y], G[j])
    V = R
    G = RG
print(max(G))
