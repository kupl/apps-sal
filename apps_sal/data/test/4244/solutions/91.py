N=int(input())
X=list(map(int,input().split()))
print(min(sum((X[j]-i)**2 for j in range(N)) for i in range(min(X),max(X)+1)))
