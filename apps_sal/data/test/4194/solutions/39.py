N, M = map(int, input().split())
m = sum(list(map(int, input().split())))
if N-m >= 0:
  print(N-m)
else:
  print("-1")
