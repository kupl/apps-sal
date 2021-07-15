import sys 
from collections import defaultdict
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())

a = [list(map(int, input().split())) for i in range(n)]
b = [[0] * m for i in range(n)]

#print(*a,*b, sep="\n")

ans = []
for i in range(n - 1):
  for j in range(m - 1):
    if a[i][j] == a[i+1][j] == a[i][j+1] == a[i+1][j+1] == 1:
      ans.append((i+1, j+1))
      b[i][j] = b[i+1][j] = b[i][j+1] = b[i+1][j+1] = 1

for i in range(n):
  for j in range(m):
    if a[i][j] != b[i][j]:
      print(-1)
      return

print(len(ans))
for i in ans:
  print(*i)
