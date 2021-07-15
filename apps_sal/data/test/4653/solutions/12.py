from sys import stdin,stdout
tt=int(stdin.readline().strip())
for t in range(tt):
    n,k=list(map(int,stdin.readline().strip().split()))
    x=n//k
    y=n-x*k
    ans=x*k+min(k//2,y)
    print(ans)



