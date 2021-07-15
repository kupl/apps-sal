n = int(input())
x0 = 0
y0 = 0
t0 = 0
for i in range(n):
  
  t, x, y = map(int, input().split())
  d = abs(x - x0) + abs (y - y0)
  if d > t - t0:
    print('No')
    return
  elif (t - t0 - d) % 2 == 1:
    print('No')
    return
  else:
    x0 = x
    y0 = y
    t0 = t

print('Yes')
