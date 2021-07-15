n,m=map(int, input().split())
a=list(map(int, input().split()))
if sum(a)<=n:
    print(n-sum(a))
else:
    print(-1)
