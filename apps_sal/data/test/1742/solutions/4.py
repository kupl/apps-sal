import sys
sys.setrecursionlimit(10 ** 5 + 1)
inf = int(10 ** 20)
max_val = inf
min_val = -inf


def RW():
    return sys.stdin.readline().strip()


def RI():
    return int(RW())


def RMI():
    return [int(x) for x in sys.stdin.readline().strip().split()]


def RWI():
    return [x for x in sys.stdin.readline().strip().split()]


(N, M) = RMI()
P = RMI()
G = [[] for x in range(N + 6)]
C = [0 for x in range(N + 6)]
ans = 0
for _ in range(M):
    (x, y) = RMI()
    G[y].append(x)
for i in range(N - 1, -1, -1):
    if C[P[i]] == N - 1 - i - ans and i != N - 1:
        ans += 1
    else:
        for F in G[P[i]]:
            C[F] += 1
print(ans)
