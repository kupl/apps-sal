a,b,x,y = list(map(int,input().split()))
if a == b:
  print(x)
  return

if a > b:
  h = a-b
  if y*(h-1) >= 2*x*(h-1):
    print((2*x*(h-1) + x))
    return
  else:
    print((y*(h-1) + x))
    return
else:
  h = b-a
  if y >= 2*x:
    print((2*x*h+x))
    return
  else:
    print((y*h+x))
    return



