A, B, K = map(int, input().split())

if A >= K:
  print(A-K, B)
elif B >= K-A:
  K -= A
  print(0, B-K)
else:
  print(0, 0)
