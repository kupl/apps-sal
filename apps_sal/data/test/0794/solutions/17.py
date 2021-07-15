n=int(input())
a=list(map(int,input().split()))
a.sort()
if sum(a)==2*sum(a[:n]):
    print(-1)
else:
    print(*a)
