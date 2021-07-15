import sys 
from collections import defaultdict
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
s = input()

sa = 0
sb = 0
a = 0
b = 0


for i in range(n):
  if s[i] == '?':
    if i < n // 2:
      a += 1
    else:
      b += 1
  else:
    if i < n // 2:
      sa += int(s[i])
    else:
      sb += int(s[i])

M = "Monocarp"
B = "Bicarp"


if sa == sb:
  if a == b:
    print(B)
    return
  else:
    print(M)
    return

if sa <= sb:
  sa, sb = sb, sa
  a, b = b, a

if a == b:
  print(M)
  return

elif a > b:
  print(M)
  return

else:
  diff = sa - sb
  x = (b - a) // 2
  #print("debug", diff, x)
  if diff == 9*x:
    print(B)
    return
  else:
    print(M)
    return


