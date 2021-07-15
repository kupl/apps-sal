import math
import collections
import itertools
import copy

def YesNo(Bool):
    if(Bool):
        print("YES")
    else:
        print("NO")
    return

def resolve():

    A,B,N=list(map(int,input().split()))
 
    X=min(N,B-1)

    ans=math.floor(A*X/B)

    print(ans)

resolve()

