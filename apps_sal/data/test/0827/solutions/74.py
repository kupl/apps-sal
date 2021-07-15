from sys import stdin, setrecursionlimit
from bisect import bisect_left, bisect_right
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop
from itertools import accumulate, combinations, combinations_with_replacement, permutations
from math import ceil, sqrt, pi, radians, sin, cos, log # log(25, 5) = 5.0
from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 7)

INF = 10 ** 18

N = int(input())
T = input()

if N == 1:
    if T == "0":
        print(10**10)
    else:
        print(10**10*2)
    return
    
if N == 2:
    if T == "00":
        print(0)
    elif T == "01":
        print(10**10-1)
    elif T == "10":
        print(10**10)
    else:
        print(10**10)
    return

def f(T):
    U = (N // 3 + 5) * "110"
    #print(U)
    for i in range(3):
        flag = True
        for j in range(len(T)):
            if T[j] != U[i + j]:
                flag = False
                break
        if flag:
            l, r = (3 - i) % 3, (i + len(T)) % 3
            tmp = (N - l - r) // 3
            if l: tmp+=1
            if r: tmp+=1
            return (10 ** 10 - tmp + 1)

    #一致せず
    return 0

print(f(T))
