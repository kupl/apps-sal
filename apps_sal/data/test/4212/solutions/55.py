import numpy as np
import itertools
N, M, Q = list(map(int, input().split()))
G = []
for i in range(Q):
    a, b, c, d = list(map(int, input().split()))
    G.append([a, b, c, d])

ans = 0

A = np.array(list(itertools.combinations_with_replacement(list(range(1, M + 1)), N)))

n = len(A)
score = np.zeros(n, np.int32)
for a, b, c, d in G:
    cond = A[:, b - 1] - A[:, a - 1] == c
    score += d * cond

print((score.max()))
