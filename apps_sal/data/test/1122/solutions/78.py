n, m = map(int, input().split())

if n%2:
  for i in range(1, m+1):
    print(i, n-i)
else:
  for i in range(1, m+1):
    if 2*i >= n/2:
      print(i, n-i-1)
    else:
      print(i, n-i)
