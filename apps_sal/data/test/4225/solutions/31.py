A, B, C, K = map(int, input().split())
if A >= K:
  print(K)
elif A+B >= K and A < K:
  print(A)
elif A+B < K:
  print(A - (K-A-B))
