import sys
input = sys.stdin.readline
for f in range(int(input())):
    x1,y1,z1=map(int,input().split())
    x2,y2,z2=map(int,input().split())
    sol=0
    foo=min(z1,y2)
    sol+=2*foo
    z1-=foo
    y2-=foo
    y1-=y2
    y1-=x2
    if y1>0:
        sol-=2*y1
    print(sol)
