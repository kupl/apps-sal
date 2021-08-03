import sys
from collections import defaultdict
t = 1
t = int(input())
for i in range(t):
    n = int(input())
    # lenn=len(n)
    a = list(map(int, sys.stdin.readline().strip().split()))
    # b=list(map(int,sys.stdin.readline().strip().split()))
    # a,b,c,d=list(sys.stdin.readline().strip().split())
    # n,k=list(map(int,sys.stdin.readline().strip().split()))

    # f=1
    # for j in range(n-1):
    #     if(a[j]==a[j+1]):
    #         continue
    #     f=0
    # if(f):
    #     print(n)
    # else:
    #     print(1)

    op = 0
    for j in range(1, n):
        if(a[j] > a[j - 1]):
            continue
        else:
            op += a[j - 1] - a[j]
    print(op)
