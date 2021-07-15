import math
n, m = map(int, input().split())
ans = 0
if n == m:
  ans = (math.factorial(n) * math.factorial(m)) * 2
elif  n + 1 == m or n == m + 1:
  ans = (math.factorial(n) * math.factorial(m))
else:
  ans = 0
ans = ans % (10 ** 9 + 7)
print(ans)
