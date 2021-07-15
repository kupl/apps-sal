x, n = map(int, input().split())

if n == 0:
  print(x)
  return
  
pp = list(map(int, input().split()))
  
for i in range(52):
  x_p = x + i
  x_m = x - i
  if x_m not in pp:
    print(x_m)
    return
  elif x_p not in pp:
    print(x_p)
    return 
