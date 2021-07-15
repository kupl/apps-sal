x, n = map(int,input().split())
L = list(map(int,input().split()))
l, r = x-1, x+1

if n == 0 or x not in L:
  print(x)
  return

while True:
  flg = True
  if l not in L:
    print(l)
    break
  elif r not in L:
    print(r)
    break
  l -= 1
  r += 1
