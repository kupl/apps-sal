import sys
import math
from collections import defaultdict
from collections import deque
from itertools import combinations
from itertools import permutations
input = lambda : sys.stdin.readline().rstrip()
read = lambda : list(map(int, input().split()))
go = lambda : 1/0
def write(*args, sep="\n"):
  for i in args:
    sys.stdout.write("{}{}".format(i, sep))
INF = float('inf')
MOD = int(1e9 + 7)
YES = "YES"
NO = "NO"

for _ in range(int(input())):
  try:
    a, b, c = read()

    ans = 0

    if a >= 1:
      a -= 1
      ans += 1
    
    if b >= 1:
      b -= 1
      ans += 1

    if c >= 1:
      c -= 1
      ans += 1

    if a >= 2:
      if b >= 1:
        a -= 1
        b -= 1
        ans += 1
      if c >= 1:
        a -= 1
        c -= 1
        ans += 1
      if b >= 1 and c >= 1:
        b -= 1
        c -= 1 
        ans += 1

    elif b >= 2:
      if a >= 1:
        a -= 1
        b -= 1
        ans += 1
      if c >= 1:
        b -= 1
        c -= 1
        ans += 1
      if a >= 1 and c >= 1:
        a -= 1
        c -= 1 
        ans += 1
        
    elif c >= 2:
      if a >= 1:
        a -= 1
        c -= 1
        ans += 1
      if b >= 1:
        b -= 1
        c -= 1
        ans += 1
      if a >= 1 and b >= 1:
        a -= 1
        b -= 1 
        ans += 1
    else:
      if a >= 1 and b >= 1:
        a -= 1
        b -= 1
        ans += 1
      if c >= 1 and b >= 1:
        c -= 1
        b -= 1
        ans += 1
      if a >= 1 and c >= 1:
        a -= 1
        c -= 1
        ans += 1
          
    if a>=1 and b>=1 and c>=1:
      ans += 1
    
    print(ans)


      
      



  except ZeroDivisionError:
    continue

  except Exception as e:
    print(e)
    continue
