from collections import defaultdict as dd
(N, K, L) = map(int, input().split())
road = [i for i in range(N)]
rail = [i for i in range(N)]


def fp(x, P):
    if x == P[x]:
        return x
    else:
        P[x] = fp(P[x], P)
        return P[x]


for i in range(K + L):
    PL = (lambda x: road if x < K else rail)(i)
    (p, q) = map(lambda x: int(x) - 1, input().split())
    (p, q) = (fp(p, PL), fp(q, PL))
    PL[p] = PL[q] = min(p, q)
Wconnected = dd(lambda: 0)
for i in range(N):
    Wconnected[fp(i, road), fp(i, rail)] += 1
print(*[Wconnected[fp(i, road), fp(i, rail)] for i in range(N)])
