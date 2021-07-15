X, K, D = map(int, input().split())
X = abs(X)

if X >= K*D:
  ans = X - K*D
else:
  l = X // D
  if (K-l) % 2 == 0:
    ans = abs(X - D*l)
  else:
    ans = abs(X - D*(l+1))
print(ans)
