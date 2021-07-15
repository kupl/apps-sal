def f(a,m):
    r=a//m
    if a%m!=0:
        r=r+1
    return r
n,m=list(map(int,input().split()))
A=list(map(int,input().split()))
B=[f(a,m) for a in reversed(A)]
print(n-B.index(max(B)))
