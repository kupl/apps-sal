from copy import deepcopy
import heapq as hq
with open(0) as f:
    (N, *a) = map(int, f.read().split())
F = [x for x in a[:N]]
C = [x for x in a[N:2 * N]]
B = [-x for x in a[2 * N:]]
hq.heapify(F)
hq.heapify(B)
memoF = [0] * (N + 1)
memoF[0] = sum(F)
memoB = [0] * (N + 1)
memoB[N] = sum(B)
for i in range(N):
    if C[i] > F[0]:
        memoF[i + 1] = memoF[i] + C[i] - hq.heapreplace(F, C[i])
    else:
        memoF[i + 1] = memoF[i]
    if -C[N - 1 - i] > B[0]:
        memoB[N - 1 - i] = memoB[N - i] - C[N - 1 - i] - hq.heapreplace(B, -C[N - 1 - i])
    else:
        memoB[N - 1 - i] = memoB[N - i]
Scores = [memoF[i] + memoB[i] for i in range(N + 1)]
ans = max(Scores)
print(ans)
