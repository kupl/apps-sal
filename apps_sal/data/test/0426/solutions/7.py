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

n, k = list(map(int, input().split()))
s = input()

if n == 1 and k > 0:
  print('0')
  return

if s[0] == '1':
  write('1', sep="")
elif (s[0] != '1' and k != 0):
  write('1', sep="")
  k -= 1
else:
  write(s[0], sep="")


for i in s[1:]:
  if i == '0':
    write('0', sep="")
  elif (i != '0' and k != 0):
    write('0', sep="")
    k -= 1
  elif i != '0' and k == 0:
    write(i, sep="")

