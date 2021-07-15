import math
import collections
import itertools
import copy

def YesNo(Bool):
    if(Bool):
        print("Yes")
    else:
        print("No")
    return

def gcd(a, b):
    """Euclidean Algorithm"""
    while b != 0:
        a, b = b, a % b
    return a

  
def lcm(a, b):
    return (a * b) // gcd(a, b)


def resolve():
    A,B,C,D=list(map(int,input().split()))

    Cmin=(A-1)//C
    Dmin=(A-1)//D
    Cmax=B//C
    Dmax=B//D
    LCM=lcm(C,D)
    LCMmin=(A-1)//LCM
    LCMmax=B//LCM

    Cnum=(Cmax - Cmin)
    Dnum=(Dmax - Dmin)
    LCMnum=(LCMmax - LCMmin)

    ans=B-(A-1) - Cnum - Dnum  +LCMnum

    print(ans)


resolve()

