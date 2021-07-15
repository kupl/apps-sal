X, K, D = map(int, input().split())
X = abs(X)
cnt = X // D
if cnt >= K:
  print(X - D * K)
  return
if (cnt % 2) ^ (K % 2) == 0:
  print(X - D * cnt)
else:
  print(abs(X - D * cnt - D))
