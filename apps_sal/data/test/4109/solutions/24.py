N, M, X = [int(_) for _ in input().split()]
A = []
C = []
for _ in range(N):
    c, *a = [int(_) for _ in input().split()]
    A.append(tuple(a))
    C.append(c)

ans = 10 ** 10
for i in range(2 ** N):
    v = [0 for _ in range(M)]
    c = 0
    for j in range(N):
        if i & 1 << j:
            for k, a in enumerate(A[j]):
                v[k] += a
            c += C[j]
    if min(v) >= X:
        ans = min(ans, c)

if ans == 10 ** 10:
    print((-1))
else:
    print(ans)
