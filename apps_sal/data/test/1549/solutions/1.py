from bisect import bisect_left as bl
import sys
(N, M, Q) = list(map(int, sys.stdin.readline().split()))
count = [0] * (M + 1)
T = tuple(map(int, sys.stdin.readline().split()))
A = []
for t in T:
    A.append(count[t] * M + t)
    count[t] += 1
A.sort()
A = [a - i for (i, a) in enumerate(A, 1)]
for _ in range(Q):
    q = int(sys.stdin.readline()) - N
    if q > A[-1]:
        q += N
    else:
        q += bl(A, q)
    sys.stdout.write(f'{(q - 1) % M + 1}\n')
