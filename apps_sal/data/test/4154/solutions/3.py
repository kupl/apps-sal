import math
import collections
import itertools

def YesNo(Bool):
    if(Bool):
        print("Yes")
    else:
        print("No")
    return

def resolve():

    N,M=list(map(int,input().split()))
    L=[0]*M
    R=[0]*M
    Lmax=0
    Rmin=10**10
    for i in range(M):
        L[i],R[i]=list(map(int,input().split()))
        Rmin=min(R[i],Rmin)
        Lmax=max(L[i],Lmax)

    print((max(0,Rmin-Lmax+1)))

resolve()

