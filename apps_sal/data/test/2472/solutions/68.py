import sys

n = int(input())
work = [list(map(int, input().split())) for i in range(n)]
work = sorted(work, key=lambda x:x[1])

sum = 0

for i in range(n):
  sum += work[i][0]
  if sum > work[i][1]:
      print('No')
      return

print('Yes')
