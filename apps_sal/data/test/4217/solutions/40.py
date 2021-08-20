import collections
import itertools
(N, M) = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]
for x in A:
    n = x.pop(0)
A = list(itertools.chain.from_iterable(A))
C = collections.Counter(A)
ct = 0
for i in range(1, M + 1):
    if C[i] == N:
        ct += 1
print(ct)
