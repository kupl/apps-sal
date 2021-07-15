import sys
n,m = map(int,input().split())
if m < 2:
  print(0)
  return
if 1 < m < n:
  print(m//2)
  return
if 2*n > m >= n:
  print(m//2)
  return
m -= 2*n
print(n+(m//4))
