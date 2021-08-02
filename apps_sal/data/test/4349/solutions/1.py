import sys

N, M = [int(x) for x in sys.stdin.readline().rstrip().split()]
K = [int(x) for x in sys.stdin.readline().rstrip().split()]
D = [0] * M
T = [0] * M
for i in range(M):
    D[i], T[i] = [int(x) for x in sys.stdin.readline().rstrip().split()]
    D[i] -= 1
    T[i] -= 1
KS = sum(K)

ok = 2 * KS
ng = KS - 1
while ok - ng > 1:
    X = (ok + ng) // 2
    last = [-1] * N
    for i in range(M):
        if last[T[i]] < D[i] < X:
            last[T[i]] = D[i]
    l2i = [[] for i in range(X)]
    for i in range(N):
        if last[i] != -1:
            l2i[last[i]].append(i)

    buy = 0
    now = 0
    for i in range(X):
        now += 1
        for j in l2i[i]:
            s = now if now < K[j] else K[j]
            now -= s
            buy += s
    buy += now // 2

    if buy >= KS:
        ok = X
    else:
        ng = X

print(ok)
