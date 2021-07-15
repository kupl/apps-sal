import sys
import math
from collections import defaultdict
from itertools import combinations
from itertools import permutations
input = lambda : sys.stdin.readline().rstrip()
read = lambda : list(map(int, input().split()))
def write(*args, sep="\n"):
  for i in args:
    sys.stdout.write("{}".format(i) + sep)
INF = float('inf')
MOD = int(1e9 + 7)

for t in range(int(input())):
  n, x= read()
  lr = sorted([list(read()) for i in range(n)], reverse = True)

  s = 0
  e = 1<<32
  while s <= e:
    m = (s + e) // 2
    money = 0
    a, b, c = [], [], [] 

    for l, r in lr:
      if l > m:
        c.append((l, r))
        money += l 
      elif r < m:
        a.append((l, r))
        money += l 
      else:
        b.append((l, r))
    
    if money > x or len(a) >= n//2 + 1:
      e = m - 1 
      continue
    
    need = n//2 + 1 - len(c)
    cnt = 0
    #print(money, a,b,c,m, sep="\n")
    for l, r in b:
      
      #print(money, cnt, need, l, r)
      if cnt < need:
        money += m  
        cnt += 1
      else:
        money += l
    if money <= x:
      s = m + 1 
    else:
      e = m - 1
  
  print(e)

    



       




    

