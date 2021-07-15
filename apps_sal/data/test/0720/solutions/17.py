from sys import stdin, stdout
from math import *
from heapq import *
from collections import *

def main():
    n=int(stdin.readline())
    a=[0]*(n+1)
    b=[0]*(n+1)
    res=1
    for i in range(1,n+1):
        a[i],b[i]=[int(x) for x in stdin.readline().split()]
        if (a[i-1]==b[i-1]):
            res+= (min(a[i],b[i])-a[i-1])
        else:
            res+=max(0,min(a[i],b[i])-max(a[i-1],b[i-1])+1)
    stdout.write(str(res))
    return 0

def __starting_point():
    main()
__starting_point()
