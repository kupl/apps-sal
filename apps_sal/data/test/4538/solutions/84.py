import math

n, d = list(map(int, input().split(' ')))
resultCnt = 0

for i in range(n):
  x, y = list(map(int, input().split(' ')))
  dis = math.sqrt((x**2) + (y**2))
  if dis <= d:
    resultCnt += 1

print(resultCnt)

