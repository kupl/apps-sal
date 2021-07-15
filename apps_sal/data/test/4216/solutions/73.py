import math

n = int(input())

def f(a, b):
  if len(str(a)) < len(str(b)):
    return len(str(b))
  else:
    return len(str(a))

ans = float('inf')
for i in range(1, int(math.sqrt(n)+1)):
  if n%i == 0:
    ans = min(ans, f(i, n//i))
print(ans)
