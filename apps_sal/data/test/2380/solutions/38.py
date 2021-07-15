#import math
#import itertools
#import numpy as np
#from collections import deque


INT = lambda: int(input())
INTM = lambda: map(int,input().split())
STRM = lambda: map(str,input().split())
STR = lambda: str(input())
LIST = lambda: list(map(int,input().split()))
LISTS = lambda: list(map(str,input().split()))

def do():
    n,m=INTM()
    A=LIST()
    bcs=[]
    for i in range(m):
        temp=LIST()
        bcs.append(temp)
    A=sorted(A)
    bcs=sorted(bcs, key=lambda x: x[1], reverse=True)
    itr=-1
    flg=False
    #print(A)
    for b,c in bcs:
        if itr+b>n-1:
            flg=True
        if flg:
            for i in range(itr+1,n):
                if A[i]<c:
                    A[i]=c
                else:
                    itr=10**9
                    break
        else:
            if A[itr+b]<c:
                A[itr+1:itr+b+1]=[c]*b
            else:
                for i in range(itr+1,itr+b+1):
                    if A[i]<c:
                        A[i]=c
                    else:
                        itr=10**9
                        break

        itr+=b

        if itr>n-1:
            break
    print(sum(A))
    #print(A)

    


def __starting_point():
    do()
__starting_point()
