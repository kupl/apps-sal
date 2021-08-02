# import itertools
# import math
from collections import deque
import sys
sys.setrecursionlimit(500 * 500)
# import numpy as np

# N = int(input())
# S = input()
# n, *a = map(int, open(0))
N, M = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# A_B = [list(map(int,input().split())) for _ in range(M)]
# S = input()

# B_C = sorted(B_C, reverse=True, key=lambda x:x[1])
# all_cases = list(itertools.permutations(P))
# a = list(itertools.combinations_with_replacement(range(1, M + 1), N))
# itertools.product((0,1), repeat=n)

# A = np.array(A)
# cum_A = np.cumsum(A)
# cum_A = np.insert(cum_A, 0, 0)

# edges = [list(map(int,input().split())) for _ in range(M)]
# tree = [[] for _ in range(N + 1)]

# for edge in edges:
#     tree[edge[0]].append([edge[1], edge[2]])
#     tree[edge[1]].append([edge[0], edge[2]])

# depth = [-1] * (N + 1)
# depth[1] = 0

# def dfs(tree, s):
#     for l in tree[s]:
#         if depth[l[0]] == -1:
#             depth[l[0]] = depth[s] + l[1]
#             dfs(tree, l[0])
# dfs(tree, 1)

# def factorization(n):
#     arr = []
#     temp = n
#     for i in range(2, int(-(-n**0.5//1))+1):
#         if temp%i==0:
#             cnt=0
#             while temp%i==0:
#                 cnt+=1
#                 temp //= i
#             arr.append([i, cnt])
#     if temp!=1:
#         arr.append([temp, 1])
#     if arr==[]:
#         arr.append([n, 1])
#     return arr

tree = [[] for _ in range(N + 1)]
edges = [list(map(int, input().split())) for _ in range(M)]

for edge in edges:
    tree[edge[0]].append(edge[1])
    tree[edge[1]].append(edge[0])

depth = [-1] * (N + 1)
depth[1] = 0

d = deque()
d.append(1)

ans = [0] * (N + 1)
while d:
    v = d.popleft()
    for i in tree[v]:
        if depth[i] != -1:
            continue
        depth[i] = depth[v] + 1
        ans[i] = v
        d.append(i)

# ans = depth[2:]
print('Yes')
print(*ans[2:], sep="\n")
