from bisect import bisect
import sys
input = sys.stdin.readline
stdout = sys.stdout


def rr():
    return input().strip()


def rri():
    return int(rr())


def rrm():
    return list(map(int, rr().split()))


N = rri()
A = rrm()
Q = rri()
A.sort()
D = sorted((A[i + 1] - A[i] for i in range(N - 1)))
P = [0]
for x in D:
    P.append(P[-1] + x)
queries = []
for q in range(Q):
    (L, R) = rrm()
    queries.append((R - L + 1, q))
queries.sort()
ans = [None] * len(queries)
i = 0
for (q, ix) in queries:
    bns = q
    i = bisect(D, q, i)
    bns += P[i] + q * (len(D) - i)
    ans[ix] = bns
print(*ans)
