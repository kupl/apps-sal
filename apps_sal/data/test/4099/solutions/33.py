n, k, m = map(int, input().split())

lst = [ int(i) for i in input().split() ]

sa = n*m

x = sum(lst)

if sa - x > k:
  print(-1)
else:
  print(max(sa-x,0))
