import itertools
import bisect
N, M = map(int, input().split())
W = list(map(int, input().split()))
V = []
for i in range(M):
    l, v = map(int, input().split())
    V.append((l, v))

V.sort(key=lambda x: x[1])
V2 = [V[i][1] for i in range(M)]
V3 = [V[i][0] for i in range(M)]
V4 = []
x = 0
for i in range(M):
    x = max(x, V3[i])
    V4.append(x)
b = V4[M - 1]

if max(W) > min(V2):
    print(-1)
    return

ans = 10**20
for k in list(itertools.permutations(range(N))):
    x = [W[k[i]] for i in range(N)]
    A = [[0] * N for _ in range(N)]
    for m in list(itertools.combinations(range(N), 2)):
        s = min(m[0], m[1])
        e = max(m[0], m[1])
        a = bisect.bisect_left(V2, sum(x[s:e + 1]))
        if a == 0:
            A[s][e] = 0
        elif a == M:
            A[s][e] = b
        else:
            A[s][e] = V4[a - 1]
    dp = [0] * N
    for i in range(1, N):
        for j in range(i):
            dp[i] = max(dp[i], dp[j] + A[j][i])
    if ans > dp[N - 1]:
        ans = dp[N - 1]
print(ans)
