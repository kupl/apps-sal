n, m = list(map(int, input().split()))

if n * 2 < m:
  print(n + (m - n * 2) // 4)
else:
  print(m // 2)
