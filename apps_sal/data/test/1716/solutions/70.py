from itertools import accumulate
import sys
input = sys.stdin.readline
(N, M, Q) = [int(x) for x in input().split()]
train = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(M):
    (L, R) = [int(x) for x in input().split()]
    train[L][R] += 1
cum = [list(accumulate(train[i])) for i in range(N + 1)]
del train
cum = list(zip(*cum))
cum = [list(accumulate(cum[j])) for j in range(N + 1)]
for _ in range(Q):
    (p, q) = [int(x) for x in input().split()]
    print(cum[q][N] - cum[q][p - 1])
