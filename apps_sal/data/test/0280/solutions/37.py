#!/usr/bin/env python3
import sys
from itertools import permutations,accumulate
from operator import itemgetter
import bisect
def input(): return sys.stdin.readline().rstrip()

def trans(l_2d):
    return [list(x) for x in zip(*l_2d)]

def main():
    n,m=list(map(int, input().split()))
    camel=list(map(int, input().split()))
    bridge=[list(map(int, input().split())) for i in range(m)]
    bridge.sort(key=itemgetter(1))
    bridge=trans(bridge)
    bridge[0]=list(accumulate(bridge[0],func=max,initial=0))
    #print(bridge)
    if max(camel) > min(bridge[1]):
        print((-1))
        return
    ans=10**15
    for permut in permutations(camel):
        graph=[[0]*n for _ in range(n)]
        for i in range(n-1):
            for j in range(i+1,n):
                weight=sum(permut[i:j+1])
                graph[i][j]=bridge[0][bisect.bisect_left(bridge[1], weight)] #n以下の個数を数える
        dist=[0]*n
        for i in range(1,n):
            mindist=0
            for j in range(i):
                mindist=max(dist[j]+graph[j][i],mindist)
            dist[i]=mindist
        ans=min(ans,dist[-1])
    #print(dist)
    print(ans)        




def __starting_point():
    main()

__starting_point()
