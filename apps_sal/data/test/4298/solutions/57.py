n,d=map(int,input().split())
k=2*d+1
if n%k==0:
    print(n//k)
else:
    print(n//k+1)
