# import itertools
# import math
# from functools import reduce
# import sys
# sys.setrecursionlimit(500*500)
# import numpy as np
# from collections import deque
# import heapq

# 入力
N = int(input())
# S = input()
# n, *a = map(int, open(0))
# H, N = map(int, input().split())
# A = list(map(int, input().split()))
# A = list(map(lambda x: int(x)*(-1), input().split()))
# B = list(map(int, input().split()))
x_y = [list(map(int, input().split())) for _ in range(N)]
# S = input()

# B_C = sorted(B_C, reverse=True, key=lambda x:x[1])
# all_cases = list(itertools.permutations(P))
# a = list(itertools.combinations_with_replacement(range(1, M + 1), N))
# itertools.product((0,1), repeat=n)

# A = np.array(A)
# cum_A = np.cumsum(A)
# cum_A = np.insert(cum_A, 0, 0)

# edges = [list(map(int,input().split())) for _ in range(N - 1)]
# tree = [[] for _ in range(N + 1)]

# for edge in edges:
#     tree[edge[0]].append(edge[1])
#     tree[edge[1]].append(edge[0])

# depth = [-1] * (N + 1)
# depth[1] = 0
# count = [0] * (N + 1)

# for i in range(Q):
#     p, x = map(int, input().split())
#     count[p] += x

# def dfs(tree, s):
#     for l in tree[s]:
#         if depth[l[0]] == -1:
#             depth[l[0]] = depth[s] + 1
#             dfs(tree, l[0])
# dfs(tree, 1)

# 素因数分解
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

# 約数列挙
# def make_divisors(n):
#     lower_divisors , upper_divisors = [], []
#     i = 1
#     while i*i <= n:
#         if n % i == 0:
#             lower_divisors.append(i)
#             if i != n // i:
#                 upper_divisors.append(n//i)
#         i += 1
#     return lower_divisors + upper_divisors[::-1]

# bfs
# tree = [[] for _ in range(N + 1)]
# edges = [list(map(int,input().split())) for _ in range(M)]

# for edge in edges:
#     tree[edge[0]].append(edge[1])
#     tree[edge[1]].append(edge[0])

# depth = [-1] * (N + 1)
# depth[1] = 0

# d = deque()
# d.append(1)

# ans = [0] * (N + 1)
# while d:
#  v = d.popleft()
#  for i in tree[v]:
#    if depth[i] != -1:
#      continue
#    depth[i] = depth[v] + 1
#    ans[i] = v
#    d.append(i)

# # ans = depth[2:]
# print('Yes')
# print(*ans[2:], sep="\n")

# def gcd_list(numbers):
#     return reduce(math.gcd, numbers)

# # 高速素因数分解準備
# MAXN = 10**6+10
# sieve = [i for i in range(MAXN+1)]
# p = 2
# while p*p <= MAXN:
#     if sieve[p] == p:
#         for q in range(2*p, MAXN+1, p):
#             if sieve[q] == q:
#                 sieve[q] = p
#     p += 1


# 45度回転
Z = []
W = []
for l in x_y:
    Z.append(l[0] + l[1])
    W.append(l[0] - l[1])

print(max((max(Z) - min(Z)), (max(W) - min(W))))
