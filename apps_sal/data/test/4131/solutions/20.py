import sys
import math
import itertools
import collections
from collections import deque
from collections import defaultdict

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD2 = 998244353
INF = float('inf')
input = lambda: sys.stdin.readline().strip()

NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()

def main():

    N, M = NMI()
        
    PY = [[m,NLI()] for m in range(M)]
    
    PY = list(sorted(list(sorted(PY,key = lambda x : x[1][1])),key = lambda x : x[1][0]))
    

    
    city = PY[0][1][0]
    cnt = 0

    for m in range(M):
        if PY[m][1][0] == city:
            cnt += 1
        else:
            city = PY[m][1][0]
            cnt = 1
            
        PY[m][1] = str(PY[m][1][0]).zfill(6) + str(cnt).zfill(6)
    
    PY = list(sorted(PY))
    
    
    for m in range(M):
        print(PY[m][1])


def __starting_point():
    main()
__starting_point()
