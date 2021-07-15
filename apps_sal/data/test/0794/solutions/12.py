n=int(input())
a=list(map(int,input().split()))
a.sort()
if sum(a[:n])!=sum(a[n:]):
    print(*a)
else:
    print(-1)
