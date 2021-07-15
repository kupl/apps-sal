n,k,m=list(map(int,input().split()))
a=list(map(int,input().split()))
if n*m-sum(a) > k:
  print((-1))
else:
  if n*m-sum(a) < 0:
    print((0))
  else:
    print((n*m-sum(a)))

