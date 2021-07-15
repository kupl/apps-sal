import sys, math
from itertools import combinations as c, product as p
from collections import deque
sys.setrecursionlimit(10**9)


def si(): return input()
def ii(): return int(input())
def fi(): return float(input())
def lstr(): return input().split()
def lint(): return list(map(int, input().split()))
def lint_dec(): return list(map(lambda x:int(x) - 1, input().split()))
def lnstr(n): return [input() for _ in range(n)]
def lnint(n): return [int(input()) for _ in range(n)]
def lint_list(n): return [lint() for _ in range(n)]



############################################################
N, M = lint()
A = lnstr(N)
B = lnstr(M)
FLG = False

for i in range(N - M + 1):
    for k in range(N - M + 1):
        if [A[j + k][i:i + M] for j in range(M)] == B:
            FLG = True
            break
    if FLG:
        break
print('Yes' if FLG else 'No')
