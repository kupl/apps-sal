n=int(input())

L=list(map(int,input().split()))
Q=0

X=[0]*1000001

for i in range(1,1000001):
    X[i]=X[i-1]^i

for i in range(1,n+1):
    Q^=L[i-1]
    x=n%i
    y=n//i
    if(y%2==1):
        Q^=X[i-1]
    Q^=X[x]
print(Q)
