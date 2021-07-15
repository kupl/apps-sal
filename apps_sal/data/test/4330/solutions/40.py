A, B = list(map(int, input().split()))
K = A + B

if K%2 == 0:
  print((K//2))
else:
  print("IMPOSSIBLE")

