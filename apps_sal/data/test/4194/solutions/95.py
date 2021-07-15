from numpy import cumsum
n,m=map(int,input().split())
l=(list(map(int,input().split())))
l=cumsum(l)[-1]
if n<l:
    print('-1')
else:
    print(n-l)
