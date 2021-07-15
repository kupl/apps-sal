import sys
input = sys.stdin.readline
for f in range(int(input())):
    n,m=map(int,input().split())
    x=n*m
    x+=1
    x//=2
    print(x)
