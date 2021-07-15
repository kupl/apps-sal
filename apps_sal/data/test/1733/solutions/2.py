from itertools import combinations,permutations
from collections import defaultdict
import math
import sys
import os

graph=defaultdict(list)

def solution(n,flo,bee):

    cleverBrute=[0]*(n+1)
    visited=[0]*(n+1)
    q=[]
    cutNode=0
    for elem in graph[flo]:
        if elem != bee:
            q.append([elem, elem])
        else:
            cutNode=elem

    visited[flo]=1
    while q:
        temp=q.pop()
        currentFrom,currentTo=temp[0],temp[1]
        visited[currentFrom]=1
        cleverBrute[currentTo]+=1
        for elem in graph[currentFrom]:
            if not visited[elem]:
                if elem != bee:
                    q.append([elem, currentTo])
                else:
                    cutNode=currentTo

    "print(cleverBrute)"
    "print(sum(cleverBrute),cleverBrute[cutNode])"
    return (sum(cleverBrute)+1-cleverBrute[cutNode])*(n-(sum(cleverBrute)+1))


def main():

    n,x,y=map(int,input().strip().split())
    for _ in range(n-1):
        u,v=map(int,input().strip().split())
        graph[u].append(v)
        graph[v].append(u)

    print(n*(n-1)-(solution(n,x,y)))


def __starting_point():
    main()


"""

3 1 3
1 2
2 3

3 1 3
1 2
1 3

"""
__starting_point()
