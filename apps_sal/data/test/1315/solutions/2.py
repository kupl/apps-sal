import math,string,itertools,fractions,heapq,collections,re,array,bisect,copy
from itertools import chain, dropwhile, permutations, combinations
from collections import defaultdict, deque

def VI(): return list(map(int,input().split()))

def run(n,a):
    b = copy.copy(a)
    for i in range(n):
        b[i] -= (n-i)
    b.sort()
    for i in range(n):
        if i<n-1:
            if b[i]==b[i+1]:
                print(":(")
                return
        b[i] = str(b[i]+(n-i))
    print(" ".join(b))


def main(info=0):
    n = int(input())
    a = VI()
    run(n,a)

def __starting_point():
    main()

__starting_point()
