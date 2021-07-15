n, k = map(int,input().split())
h = list(map(int,input().split()))
h.sort()
if n <= k:
  print("0")
else:
  if k == 0:
    ans = sum(h)
  else:
    x = n - k
    ans = sum(h[:x])

  print(ans)
