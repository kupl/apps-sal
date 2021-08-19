import sys
sys.setrecursionlimit(10 ** 7)
(N, M) = list(map(int, input().split()))
R = [[] for _ in range(N)]
for _ in range(M):
    (a, b, c) = list(map(int, input().split()))
    R[a - 1].append((b - 1, c))
INF = 10 ** 40
S = [-INF] * N
S[0] = 0


def score(fst, s, C):
    for (nx, p) in R[fst]:
        if S[nx] >= s + p or S[nx] >= INF:
            continue
        S[nx] = s + p
        if nx in C:
            S[nx] = INF
        C[nx] = C.get(nx, 0) + 1
        score(nx, S[nx], C)
        C[nx] -= 1
        if C[nx] == 0:
            del C[nx]


score(0, 0, {0: 1})
if S[-1] < INF:
    ans = S[-1]
else:
    ans = 'inf'
print(ans)
