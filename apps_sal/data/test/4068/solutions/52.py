#import math
#import itertools
#import numpy as np
#from collections import deque
# sys.setrecursionlimit(10 ** 6)
MOD = 10 ** 9 + 7
#INF = 10 ** 9
#PI = 3.14159265358979323846

INT = lambda: int(input())
INTM = lambda: map(int,input().split())
STRM = lambda: map(str,input().split())
STR = lambda: str(input())
LIST = lambda: list(map(int,input().split()))
LISTS = lambda: list(map(str,input().split()))

def do():
    n,m=INTM()
    b_sts=[False]*n
    for i in range(m):
        b=INT()
        b-=1
        b_sts[b]=True
        
    step=[0]*(n+2)
    step[1]=1
    for i in range(n):
        if b_sts[i]:
            continue
        else:
            step[i+2]=(step[i+1]+step[i])%MOD
    print(step[-1]%MOD)

def __starting_point():
    do()
__starting_point()
