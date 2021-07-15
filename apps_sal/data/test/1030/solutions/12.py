import math,string,itertools,fractions,heapq,collections,re,array,bisect
from itertools import chain, dropwhile, permutations, combinations
from collections import defaultdict


def main(n,p,k):
    x = range(p-k,p+k+1)
    x = [j for j in x if j >=1 and j <= n]
    if 1 not in x:
        print("<< ",end="")
    for j in range(max(1,p-k),p):
        print(str(j),end=" ")
    print("("+str(p)+") ",end="")
    for j in range(p+1,min(p+k,n)+1):
        print(str(j),end=" ")
    if n not in x:
        print(">>")


def main_input(info=0):
    n,p,k = map(int,input().split())
    #t = [(int(x)-1,i+1) for i,x in enumerate(input().split())]
    #l,r = list(range(n)), list(range(n))
    #for i in range(n):
    #    l[i],r[i] = map(int,input().split())
#    t = [map(int,input().split()) for x in range(n)]
    main(n,p,k)

def __starting_point():
    main_input()

__starting_point()
