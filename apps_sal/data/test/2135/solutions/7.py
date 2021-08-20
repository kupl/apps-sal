from itertools import accumulate
import math
import bisect


def list_sum(L1, L2):
    return [L1[i] + L2[i] for i in range(len(L1))]


(h, w) = [int(x) for x in input().split()]
M = []
for i in range(h):
    M.append([1 if c == '.' else 0 for c in input().rstrip()])
H = [[0] + list(accumulate((M[i][j] and M[i][j + 1] for j in range(w - 1)))) for i in range(h)]
V = [[0] + list(accumulate((M[i][j] and M[i + 1][j] for i in range(h - 1)))) for j in range(w)]
Hsum = list(accumulate(H, list_sum))
Vsum = list(accumulate(V, list_sum))


def can(a, b):
    return Hsum[a][b] + Vsum[b][a]


def query(a1, b1, a2, b2):
    return can(a2, b2) + can(a1, b1) - can(a1, b2) - can(a2, b1) + H[a1][b2] - H[a1][b1] + V[b1][a2] - V[b1][a1]


q = int(input())
for i in range(q):
    (a1, b1, a2, b2) = [int(x) - 1 for x in input().split()]
    print(query(a1, b1, a2, b2))
