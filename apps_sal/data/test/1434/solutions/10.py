import math,string,itertools,fractions,heapq,collections,re,array,bisect
from itertools import chain, dropwhile, permutations, combinations
from collections import defaultdict


def main2(n,d,s,info=0):
    # correct, but slow
    edges = []
    m = mm = sum(d)//2
    while m>0:
        f = [x for x in zip(d,list(range(n))) if x[0]==1]
        for _,i in f:
            if d[i]==1:
                d[i] = 0
                d[s[i]] -= 1
                s[s[i]] ^= i
                m -= 1
                edges.append([i,s[i]])
    print(mm)
    for u,v in edges:
        print(u,v)

def main(n,d,s,info=0):
    edges = []
    curr = []
    for i in range(n):
        if d[i]==1: curr.append(i)
    while len(curr):
        i = curr.pop()
        if d[i]==1:
            d[i] = 0
            d[s[i]] -= 1
            s[s[i]] ^= i
            edges.append([i,s[i]])
            if d[s[i]] == 1:
                curr.append(s[i])
    print(len(edges))
    for u,v in edges:
          print(u,v)

def main_input(info=0):
    n = int(input())
    d,s = list(range(n)), list(range(n))
    for i in range(n):
        d[i],s[i] = list(map(int,input().split()))
    main(n,d,s,info=info)

def __starting_point():
    main_input()

__starting_point()
