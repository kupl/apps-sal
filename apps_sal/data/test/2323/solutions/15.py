from bisect import bisect
import sys
input = sys.stdin.readline
stdout = sys.stdout
rr = lambda: input().strip()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().strip().split()))


N = rri()
A = rrm()
Q = rri()
A.sort()
D = sorted(A[i + 1] - A[i] for i in range(N - 1))
P = [0]
for x in D:
    P.append(P[-1] + x)

queries = []
for q in range(Q):
    L, R = rrm()
    queries.append((R - L + 1, q))
queries.sort()
ans = [None] * len(queries)

i = 0
for q, ix in queries:
    bns = q
    # bns += sum(min(d, w) for d in D)
    i = bisect(D, q, i)
    bns += P[i] + q * (len(D) - i)
    ans[ix] = bns

print(*ans)
