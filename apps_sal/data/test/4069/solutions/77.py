X, K, D =map(int,input().split())
X = abs(X)

if X > K*D:
  print(X-K*D)
else:
  greed = X//D
  if (K - greed)%2 == 0:
    print(X-greed*D)
  else:
    print((1+greed)*D -X)
