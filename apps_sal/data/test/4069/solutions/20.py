X,K,D=map(int,input().split())
X=abs(X)
r=X//D
if r>=K:
  print(X-K*D)
  return
if (K-r)%2==0:
  print(X-r*D)
else:
  print(abs(X-r*D-D))
