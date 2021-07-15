# import itertools
# import math
# import sys
# sys.setrecursionlimit(500*500)
# import numpy as np

# N = int(input())
# S = input()
# n, *a = map(int, open(0))
N, K = map(int, input().split())
P = list(map(int, input().split()))
# B = list(map(int, input().split()))
# tree = [[] for _ in range(N + 1)]
# B_C = [list(map(int,input().split())) for _ in range(M)]
# S = input()

# B_C = sorted(B_C, reverse=True, key=lambda x:x[1])
# all_cases = list(itertools.permutations(P))
# a = list(itertools.combinations_with_replacement(range(1, M + 1), N))
# itertools.product((0,1), repeat=n)

# A = np.array(A)
# cum_A = np.cumsum(A)
# cum_A = np.insert(cum_A, 0, 0)

# def dfs(tree, s):
#     for l in tree[s]:
#         if depth[l[0]] == -1:
#             depth[l[0]] = depth[s] + l[1]
#             dfs(tree, l[0])
# dfs(tree, 1)

E = [0]
tot = 0
for p in P:
    tot += (p + 1) / 2
    E.append(tot)


m = 0
for i in range(N - (K - 1)):
    _ = E[i + K] - E[i]
    if _ > m:
        m = _

print(m)
