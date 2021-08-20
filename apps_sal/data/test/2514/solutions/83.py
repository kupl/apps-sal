(_, A, Q, *X) = open(0)
S = 0
L = [0] * 7 ** 6
for a in map(int, A.split()):
    S += a
    L[a] += 1
for x in X:
    (B, C) = map(int, x.split())
    S += (C - B) * L[B]
    L[C] += L[B]
    L[B] = 0
    print(S)
