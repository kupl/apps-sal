import sys
from collections import defaultdict
from itertools import combinations
from itertools import permutations
input = lambda : sys.stdin.readline().rstrip()
def write(*args, sep=" "):
  for i in args:
    sys.stdout.write("{}".format(i) + sep)
INF = float('inf')
MOD = int(1e9 + 7)

for t in range(int(input())):
  n = int(input())
  arr = list(map(int, input().split()))
  d = defaultdict(int) 

  for i in arr:
    d[i] += 1
  
  for i in range(0, 11):
    x = d[1 << i] // 2
    d[1 << (i + 1)] += x 
  if d[2048]:
    print("YES")
  else:
    print("NO")


