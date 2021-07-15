import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N):
    read_all = [tuple(map(int, input().split())) for _ in range(N)]
    return map(list,zip(*read_all))

#################

L = I()

N = math.floor(math.log2(L))+1
M = 0
edge = []
for i in range(N-1):
    edge.append([i,i+1,0])
    edge.append([i,i+1,2**i])
    M += 2
for i in range(N-1)[::-1]:
    if L-2**i >= 2**(N-1):
        edge.append([i,N-1,L-2**i])
        M += 1
        L -= 2**i

print(N,M)
for e in edge:
    print(e[0]+1, e[1]+1, e[2])
