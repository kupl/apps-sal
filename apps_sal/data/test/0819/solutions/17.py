n, k = map(int, input().split())
l = [int(x) for x in input().split()]
sl = []
sr = [0 for i in range(n)]
m = -10000000000
if k == 1:
  print(min(l))
elif k > 2:
  print(max(l))
else:
  sl.append(l[0])
  for i in range(1, n):
    sl.append(min(sl[i-1], l[i]))
    
  sr[n-1] = l[n-1]
  for i in range(n-2, -1, -1):
    sr[i] = min(sr[i+1], l[i])

  for i in range(0, n-1):
    m = max(m, sl[i], sr[i+1])

  print(m)
