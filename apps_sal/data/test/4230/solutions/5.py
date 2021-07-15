x,n = map(int,input().split())
if n != 0:
  p = list(map(int,input().split()))
  sa = 102
  ans = []
  for i in range(x,102):
    if i not in p:
      if sa > i-x:
        sa = i-x
        ans = i
      elif sa == i-x:
        if ans > i:
          ans = i
  for i in range(x):
    if x-i-1 not in p:
      if sa > i+1:
        sa = i+1
        ans = x-i-1
      elif sa == i+1:
        if ans > x-i-1:
          ans = x-i-1
  print(ans)
else:
  print(x)
