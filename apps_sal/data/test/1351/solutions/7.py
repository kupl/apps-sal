import sys
from collections import defaultdict
from itertools import combinations
from itertools import permutations
input = lambda : sys.stdin.readline().rstrip()
def write(*args, sep="\n"):
  for i in args:
    sys.stdout.write("{}".format(i) + sep)
INF = float('inf')
MOD = int(1e9 + 7)

l, r = map(int, input().split())

for i in range(l, r+1):
  if len(set(str(i))) == len(str(i)):
    print(i)
    return

print("-1")
