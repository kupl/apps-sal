import sys
sys.setrecursionlimit(10 ** 9)
(N, Q) = map(int, input().split())
T = [[] for _ in range(N)]
for _ in range(N - 1):
    (a, b) = map(int, input().split())
    T[a - 1].append(b - 1)
    T[b - 1].append(a - 1)
S = [0] * N
for _ in range(Q):
    (p, x) = map(int, input().split())
    S[p - 1] += x


def search(p, q=-1):
    for a in T[p]:
        if a != q:
            S[a] += S[p]
            search(a, p)


search(0)
print(*S)
