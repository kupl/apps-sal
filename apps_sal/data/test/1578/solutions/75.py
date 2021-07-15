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

    N=int(input())
    ans=((N)*(N-1))

    print((ans//2))

resolve()

