import math

m,R = list(map (int,input().split()))

D = math.sqrt (2) * R
result = 0

def sum_dist (n):
  return n*(n+1)*R + 2*D*n

for i in range (1,m+1):
  result += 2*R
  if i-1   > 0: result += 2*R + D
  if m-i   > 0: result += 2*R + D
  if i-2   > 0: result += sum_dist (i-2)
  if m-i-1 > 0: result += sum_dist (m-i-1)

print(result / m / m)

