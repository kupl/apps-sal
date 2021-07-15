#!/usr/bin/env python3
import sys
def input(): return sys.stdin.readline().rstrip()


def main():
    n=int(input())
    A=list(map(int, input().split()))
    counts=[0]*(10**6+5)
    for AA in A:
        counts[AA]+=1
    ans=0
    for i in range(1,10**6+5):
        if counts[i]>0:
            for j in range(i+i,10**6+5,i):
                counts[j]=-1
        if counts[i]==1:
            ans+=1
    print(ans)
        

        
    


def __starting_point():
    main()


__starting_point()
