N, M, X = map(int, input().split())
C = []
A = []
for _ in range(N):
    l = list(map(int, input().split()))
    C.append(l[0])
    A.append(l[1:])
 
ans = -1
for i in range((1<<N)):
    u = [0] * M
    p = 0
    for j in range(N):
        if i & (1 << j):
            p += C[j]
            for k in range(M):
                u[k] += A[j][k]
    if min(u) >= X:
        if ans == -1 or ans > p:
            ans = p
print(ans)
