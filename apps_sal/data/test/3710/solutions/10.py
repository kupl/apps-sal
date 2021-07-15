# *********************************************************************
# *-------------------------------------------------------------------*
# *                                                                   *
# *   Life is just a life. Lead it, Feel it & Enjoy It Properly.      *
# *   Nothing is impossible. Just believe in yourself & Almighty.     *
# *                                                                   *
# *-------------------------------------------------------------------*
# *********************************************************************
import math

def LCM(a,b):
    return int(a/math.gcd(a,b))*b

def DenTofieM():
    n, k = list(map(int,input().split()))
    ar = list(map(int,input().split()))

    L=1
    for i in ar:
        G=math.gcd(i,k)
        L=LCM(L,G)
    if L==k: print("Yes")
    else: print("No")

DenTofieM()


