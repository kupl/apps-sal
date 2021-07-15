q=int(input())
for i in range(q):
    n,k=list(map(int,input().split()))
    y=n%k
    print((n//k)*k+min(y,k//2))

