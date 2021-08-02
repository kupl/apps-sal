N, M, X = map(int, input().split())
C = []
A = []
for i in range(N):
    a = [int(i) for i in input().split()]
    C.append(a[0])
    del a[0]
    A.append(a)
ans = M * (10**5) + 1
for i in range(2**N):
    bi = format(i, "b")
    bistr = str(bi)
    P = ["0"] * N
    Q = [0] * M
    m = 0
    for j in range(len(bistr)):
        P[-1 - j] = bistr[-1 - j]
    for j in range(N):
        if(P[j] == "1"):
            m += C[j]
            for k in range(M):
                Q[k] += A[j][k]
    count = 0
    for j in range(M):
        if(Q[j] >= X):
            count += 1
        if(count >= M):
            ans = min(ans, m)
if(ans >= M * (10**5) + 1):
    print(-1)
    return
print(ans)
