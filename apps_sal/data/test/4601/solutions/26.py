n,k = map(int,input().split())
h = list(map(int,input().split()))
ans = 0

if(n <= k):
  print(0)
else:
  h.sort()
  a = []
  a = h[:n-k]
  print(sum(a))
