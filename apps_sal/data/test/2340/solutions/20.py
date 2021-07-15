import sys

q = int(input())
for _ in range(q):
  h, n = list(map(int, sys.stdin.readline().split()))
  p = iter(list(map(int, sys.stdin.readline().split())) + [0])
  cost = 0
  akt = next(p)
  a = next(p)
  if a == 0:
    print(0)
  else:
    b = next(p)
    while True:
      if a-b == 1:
        akt = b
        if akt == 0:
          break
        else:
          a = next(p)
        if a == 0:
          break
        else:
          b = next(p)
      else:
        cost += 1
        akt = a-1
        a = b
        if a == 0:
          break
        else:
          b = next(p)
    print(cost)

