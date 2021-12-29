from operator import add
(N, M, X) = map(int, input().split())
C = []
A = []
for i in range(N):
    T = list(map(int, input().split()))
    C.append(T[0])
    A.append(T[1:])
ans = 100000000
for i in range(2 ** N):
    ex = [0] * M
    cost = 0
    Flag = True
    for j in range(N):
        if i >> j & 1:
            ex = list(map(add, ex, A[j]))
            cost += C[j]
    for k in range(M):
        if not ex[k] >= X:
            Flag = False
    if Flag:
        if cost <= ans:
            ans = cost
if ans == 100000000:
    print(-1)
else:
    print(ans)
