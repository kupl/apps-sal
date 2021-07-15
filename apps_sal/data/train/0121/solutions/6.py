import math
for _ in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    li.sort()
    print(li[n]-li[n-1])
