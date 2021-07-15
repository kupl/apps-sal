#import math
#import itertools
import numpy as np
#from collections import deque

INT = lambda: int(input())
INTM = lambda: map(int,input().split())
STRM = lambda: map(str,input().split())
STR = lambda: str(input())
LIST = lambda: list(map(int,input().split()))
LISTS = lambda: list(map(str,input().split()))

def do():
    n,m=INTM()
    ls=[]
    rs=[]
    for i in range(m):
        l,r=INTM()
        ls.append(l)
        rs.append(r)
    
    ans=min(rs)-max(ls)+1
    if ans<=0:
        ans=0
    print(ans)



    
def __starting_point():
    do()
__starting_point()
