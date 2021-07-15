# alpha = "abcdefghijklmnopqrstuvwxyz"
# prime = 998244353 
INF = 100_000_000
# from heapq import heappush, heappop
from collections import defaultdict
t = 1#int(input())
# from math import sqrt


for test in range(t):
    n = int(input())
    # n,m = (map(int, input().split()))
    # a = []
    # for i in range(n):
    q = (list((list(map(int, input().split())))))

    p = [n for i in range(n)]

    for i in range(1, n):
        p[i] = q[i-1]+p[i-1]
    
    t = list(p)
    t.sort()
    tmp = t[0]-1
    ans = 0
    for i in range(n):
        p[i] = p[i]-tmp
        if t[i]-tmp!=i+1:
            ans=-1
            break
    if ans==-1:
        print(ans)
    else:
        print(*p)





    










