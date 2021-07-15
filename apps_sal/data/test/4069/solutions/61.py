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

    X,K,D=list(map(int,input().split()))

    ans=0
    if(abs(X)-K*D<0):
        tmp=X//D
        if((K-tmp)%2==0):
            ans=abs(X-D*tmp)
        else:
            ans=abs(X-D*(tmp+1))
    else:
        ans=abs(X)-K*D

    print(ans)
resolve()

