n,k = map(int, input().split())
h = list(map(int, input().split()))
if k >= len(h):
  print(0)
else:
  h.sort()
  print(sum(h[:n-k]))
