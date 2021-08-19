# import itertools
# import math
# import sys
# sys.setrecursionlimit(500*500)
# import numpy as np
# from collections import deque
import heapq

# N = int(input())
# S = input()
# n, *a = map(int, open(0))
N, M = list(map(int, input().split()))
A = list([int(x) * (-1) for x in input().split()])
# B = list(map(int, input().split()))
# tree = [[] for _ in range(N + 1)]
# B_C = [list(map(int,input().split())) for _ in range(M)]
# S = input()

# A = sorted(A, reverse=True)
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

heapq.heapify(A)
for i in range(M):
    max_num = heapq.heappop(A) * (-1)
    heapq.heappush(A, (-1) * (max_num // 2))

A = [x * (-1) for x in A]
print((sum(A)))
