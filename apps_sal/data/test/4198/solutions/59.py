import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time, copy

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces

A, B, X = na()

def judge(N, A, B, X):
    dn = len(str(N))
    if A * N + B * dn <= X:
        return True
    else:
        return False

def binary_search(A, B, X):
    left = 0
    right = 10 ** 9
    while right - left > 1:
        mid = left + (right - left) // 2
        if judge(mid, A, B, X):
            left = mid
        else:
            right = mid
    return left

if judge(10 ** 9, A, B, X):
    print(10 ** 9)
else:
    print(binary_search(A, B, X))
