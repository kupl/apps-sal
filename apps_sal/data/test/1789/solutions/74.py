import math
import numpy as np
import sys
input = sys.stdin.readline

def main():
    a, b, x, y = list(map(int,input().split()))
    if(b>a):
        d = b-a
        t1=y*d+x
        t2=2*x*d+x
        print(min(t1, t2))
    elif(a==b):print(x)
    else:
        d=a-b
        t1=y*(d-1)+x
        t2=2*x*(d-1)+x
        print(min(t1, t2))

main()
