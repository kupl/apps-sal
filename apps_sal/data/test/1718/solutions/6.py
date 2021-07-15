n, k = map(int, input().split())
a = list(map(int, input().split()))

if n == k:
  print(1)
else:
  print(-(-(n-1)//(k-1)))
