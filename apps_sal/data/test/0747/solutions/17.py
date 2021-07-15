n, x1 = map(int, input().split())
class Candy:
  t = 0
  h = 0
  m = 0
candy0 = []
candy1 = []
for i in range(n):
  candy = Candy()
  candy.t, candy.h, candy.m = map(int, input().split())
  if candy.t == 0:
    candy0.append(candy)
  else:
    candy1.append(candy)

def sortfn(item):
  return item.m

def getnext(items, x):
  for item in items:
    if item.h <= x:
      return item
  val = Candy()
  val.h = x + 1
  return val

candy0.sort(key = sortfn, reverse = True)
candy1.sort(key = sortfn, reverse = True)

count0 = 0
count1 = 0

def getcount(candy0, candy1):
  count = 0
  next = candy0
  x = x1
  while getnext(next, x).h <= x:
    nextitem = getnext(next, x)
    x += nextitem.m
    count += 1
    next.remove(nextitem)
    if next == candy0:
      next = candy1
    else:
      next = candy0
  return count

count0 = getcount(candy0.copy(), candy1.copy())
count1 = getcount(candy1.copy(), candy0.copy())

print(max(count0, count1))
