X,K,D = list(map(int,input().split()))
X = abs(X)
if X-D*K>=0:
  print((X-D*K))
else:
  r = X//D
  print((abs(X-D*(r+(r+K)%2))))

