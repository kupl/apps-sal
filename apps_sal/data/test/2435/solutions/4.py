import sys
input = sys.stdin.readline
for f in range(int(input())):
    n,x,m=map(int,input().split())
    l=x
    r=x
    for i in range(m):
        li,ri=map(int,input().split())
        if li<=r and ri>=l:
            l=min(l,li)
            r=max(r,ri)
    print(r-l+1)
