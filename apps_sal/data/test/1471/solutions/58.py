# import itertools
# import math
import sys
sys.setrecursionlimit(500 * 500)
# import numpy as np

N = int(input())
# S = input()
# n, *a = map(int, open(0))
# H, W, K = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# S = input()

# d = sorted(d, reverse=True, key=lambda x:x[0])
# all_cases = list(itertools.permutations(P))
# a = list(itertools.combinations_with_replacement(range(1, M + 1), N))
# itertools.product((0,1), repeat=n)

# A = np.array(A)
# cum_A = np.cumsum(A)
# cum_A = np.insert(cum_A, 0, 0)

edges = [list(map(int, input().split())) for _ in range(N - 1)]
tree = [[] for _ in range(N + 1)]

for edge in edges:
    tree[edge[0]].append([edge[1], edge[2]])
    tree[edge[1]].append([edge[0], edge[2]])

# print(tree)

depth = [-1] * (N + 1)
depth[1] = 0


def dfs(tree, s):
    for l in tree[s]:
        if depth[l[0]] == -1:
            depth[l[0]] = depth[s] + l[1]
            dfs(tree, l[0])


dfs(tree, 1)

# print(depth)

for l in depth[1:]:
    if l % 2 == 0:
        print((1))
    else:
        print((0))
