n,m=map(int,input().split())
X=list(map(int,input().split()))
Y=list(map(int,input().split()))
xsum=0;ysum=0;mod=10**9+7
for i,x in enumerate(X): xsum+=x*(i-(n-1-i))
for i,y in enumerate(Y): ysum+=y*(i-(m-1-i))
print(xsum * ysum % mod)
