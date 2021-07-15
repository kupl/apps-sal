ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq

H,W=ma()
def f(H,W):
    ret=10**10+5
    for h in range(1,H):
        s1 = h*W
        s2,s3 = (H-h)//2*W,(H-h+1)//2*W
        ret=min(ret,max(s1,s2,s3) -min(s1,s2,s3) )
        s2,s3 = W//2*(H-h),(W+1)//2*(H-h)
        ret=min(ret,max(s1,s2,s3) -min(s1,s2,s3) )
    return ret
print(min(f(H,W),f(W,H)))

