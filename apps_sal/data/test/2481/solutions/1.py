import sys
sys.setrecursionlimit(2147483647)
input=sys.stdin.readline
import math
from heapq import heappush, heappop

def solve(h,w,tables,A):
  for i in range(10):
    for j in range(10):
      for k in range(10):
        tables[j][k] = min(tables[j][k], tables[j][i] + tables[i][k])
  cost = 0
  for i in range(h):
    for j in range(w):
      p = A[i][j]
      if p == -1:
        continue
      cost += tables[p][1]
  return cost
  

def main():
  h, w = map(int, input().split(' '))
  tables = []
  for i in range(10):
    tables.append(list(map(int, input().split(' '))))
  A = []
  for _ in range(h):
    A.append(list(map(int, input().split(' '))))
  ans = solve(h, w, tables, A)
  print(ans)
  

def __starting_point():
  main()
__starting_point()
