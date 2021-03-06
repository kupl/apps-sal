from itertools import zip_longest
from heapq import heappush, heappop
Q = int(input())
(q, a, b) = zip_longest(*(list(map(int, input().split())) for _ in range(Q))) if Q else ((), ())
INF = 10 ** 18
L = []
R = []
heappush(L, INF)
heappush(R, INF)
S = 0
res = []
for (i, A, B) in zip(q, a, b):
    if i == 1:
        S += B
        if len(L) == len(R):
            if A < -L[0]:
                S += -L[0] - A
                heappush(L, -A)
            elif A <= R[0]:
                heappush(L, -A)
            else:
                S += A - R[0]
                t = heappop(R)
                heappush(L, -t)
                heappush(R, A)
        elif A < -L[0]:
            S += -L[0] - A
            t = -heappop(L)
            heappush(R, t)
            heappush(L, -A)
        else:
            S += A - -L[0]
            heappush(R, A)
    else:
        res.append((-L[0], S))
ans = '\n'.join((' '.join(map(str, r)) for r in res))
print(ans)
