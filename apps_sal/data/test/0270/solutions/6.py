N, M = list(map(int, input().split()))
st = [list(map(int, input().split())) for _ in range(M)]

R = {}
for s, t in st:
    s -= 1
    t -= 1
    if s in R:
        R[s].append(t)
    else:
        R[s] = [t]

DP = [0] * N
ans = N
D = [0] * N
for i in range(N - 2, -1, -1):
    ma = 0
    su = 0
    le = len(R[i])
    for j in R[i]:
        su += DP[j]
        ma = max(ma, DP[j])

    DP[i] = su / le + 1
    if le == 1:
        D[i] = 0
    else:
        D[i] = DP[i] - (((su - ma) / (le - 1)) + 1)

P = [0] * N
P[0] = 1
ma = 0
man = -1
for i in range(N - 1):
    t = P[i] / len(R[i])
    for j in R[i]:
        P[j] += t
    t = P[i] * D[i]
    R[i].sort()
    if ma < t:
        ma = t
        man = i

if ma == -1:
    print((DP[0]))
else:
    print((DP[0] - ma))
