N, C = list(map(int, input().split()))

xv = [tuple(map(int, input().split())) for i in range(N)]
xv2 = [(C - x, v)for x, v in xv[::-1]]


L = [0]*N
ans = 0
for i, X in enumerate(xv):
    x, v = X
    L[i] = L[i-1] + v
R = [0]*N
for i in range(N):
    L[i] -= xv[i][0]
for i, X in enumerate(xv2):
    x, v = X
    R[i] = R[i-1] + v
for i in range(N):
    R[i] -= xv2[i][0]

LL = [0]*(N+1)
RR = [0]*(N+1)
for i in range(N):
    LL[i+1] = max(LL[i], L[i])
    RR[i+1] = max(RR[i], R[i])

ans = 0
ans = max(ans, LL[-1])
ans = max(ans, RR[-1])
for i in range(N):
    ans = max(ans, LL[N - 1 - i] + R[i] - xv2[i][0])
    ans = max(ans, RR[N - 1 - i] + L[i] - xv[i][0])
print(ans)

