x, n = map(int,input().split())
L = list(map(int,input().split()))

if n == 0 or x not in L:
  print(x)
  return

for i in range(102):
  if (x-i) not in L:
    print(x-i)
    break
  elif (x+i) not in L:
    print(x+i)
    break
