import math
n = int(input())

def k(p):
  c = 0
  while p > 0:
    c += 1
    p //= 10
  return c

res = 100
for i in range(1,int(math.sqrt(n)) + 5):
  if n % i == 0:
    res = min( max(k(i), k(n//i)), res)

print(res)
