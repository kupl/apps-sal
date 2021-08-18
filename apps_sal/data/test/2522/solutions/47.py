N = int(input())
A = [int(a) for a in input().split()]
B = [int(a) for a in input().split()]
C = [0] * N
D = [0] * N
c = d = 0
for i in range(N):
    a = A[i]
    b = B[i]
    if C[a - 1] == 0:
        for j in range(c, a):
            C[j] = C[c]
        c = a - 1
        C[c] = C[c - 1] + 1
    else:
        C[a - 1] += 1
    if D[b - 1] == 0:
        for j in range(d, b):
            D[j] = D[d]
        d = b - 1
        D[d] = D[d - 1] + 1
    else:
        D[b - 1] += 1
for j in range(c, N):
    C[j] = C[c]
for j in range(d, N):
    D[j] = D[d]
E = [0] * N
for i in range(N):
    if i == 0:
        E[i] = C[i] + D[i]
    else:
        E[i] = C[i] - C[i - 1] + D[i] - D[i - 1]
if max(E) > N:
    print("No")
else:
    for i in range(N):
        if i == 0:
            x = C[i]
        if x < C[i] - D[i - 1]:
            x = C[i] - D[i - 1]
    B_ = [0] * N
    for i in range(N):
        B_[(i + x) % N] = B[i]
    print("Yes")
    print(*B_, sep=' ')
