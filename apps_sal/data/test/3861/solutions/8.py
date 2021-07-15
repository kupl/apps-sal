from math import *
def is_it_square(x):
  if x<0:
    return False
  return floor(sqrt(x))**2 == x

n=int(input())
l=[int(x) for x in input().split()]
l.sort()
l.reverse()
for x in l:
  if is_it_square(x):
    continue
  print(x)
  return
