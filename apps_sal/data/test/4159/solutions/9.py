import sys
a,b,k = map(int,input().split())

if a >= k:
  print(a-k,b)
  return

if b >= (k-a):
  print(0,b-(k-a))
  return

print(0,0)
