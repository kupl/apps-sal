q=int(input())
for i in range(q):
    n,k=map(int,input().split())
    ans=n//k*k+min(n%k,k//2)
    print(ans)
