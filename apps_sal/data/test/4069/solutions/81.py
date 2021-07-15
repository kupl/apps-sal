def pm(x):
  if x>=0:
    return 1
  else:
    return -1
X,K,D=map(int,input().split())
if (abs(X))<D :
  if K%2==0:
    print(int(abs(X)))
  else:
    a=X-pm(X)*D
    print(int(abs(a)))
else:
  if abs(X)//D>=K:
    a=X-(pm(X))*D*K
    print(int(abs(a)))
  else:
    K=K-int(abs(X)//D)
    X=X-(pm(X))*D*int(abs(X)//D)
    if (abs(X))<D :
      if K%2==0:
        print(int(abs(X)))
      else:
        a=X-(pm(X))*D
        print(int(abs(a)))
