# import itertools
# import math
# from functools import reduce
# import sys
# sys.setrecursionlimit(500*500)
# import numpy as np
# import heapq
# from collections import deque

K = int(input())
# S = input()
# n, *a = map(int, open(0))
# N, M = map(int, input().split())
# A = list(map(int, input().split()))
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

# def gcd_list(numbers):
#     return reduce(math.gcd, numbers)

# if gcd_list(A) > 1:
#     print("not coprime")
#     return

# 高速素因数分解準備
#MAXN = 10**6+10
#sieve = [i for i in range(MAXN+1)]
#p = 2
#while p*p <= MAXN:
#    if sieve[p] == p:
#        for q in range(2*p, MAXN+1, p):
#            if sieve[q] == q:
#                sieve[q] = p
#    p += 1

cand = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
for i in range(9):
    tmp = []
    for val in cand[-1]:
        if str(val)[-1] != "0":
            tmp.append(val * 10 + int(str(val)[-1]) - 1)
        tmp.append(val * 10 + int(str(val)[-1]))
        if str(val)[-1] != "9":
            tmp.append(val * 10 + int(str(val)[-1]) + 1)
    cand.append(tmp)
        
ans = []
for l in cand:
    for i in l:
        ans.append(i)

ans.sort()
print(ans[K - 1])
