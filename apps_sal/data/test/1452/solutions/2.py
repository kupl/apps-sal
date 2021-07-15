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

r, c = list(map(int, input().split()))

row = list(map(int, input().split()))
column = list(map(int, input().split()))
arr = [ [-1] * (c + 1) for i in range(r + 1) ]

for i in range(r):
  for j in range(row[i]):
      arr[i][j] = 1
    
  arr[i][row[i]] = 0

  #print(arr, "!")

for j in range(c):
  #print(arr)
  for i in range(column[j]):
    if arr[i][j] != 0:
      arr[i][j] = 1
    else:
      print(0)
      return
  
  if arr[column[j]][j] == 1:
    print(0)
    return
  
  arr[column[j]][j] = 0

cnt = 0
for i in range(r):
  for j in range(c):
    cnt += (arr[i][j] == -1)

#print("???", cnt)
print(pow(2, cnt, MOD))

