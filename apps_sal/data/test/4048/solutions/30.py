import math

ans = 1000000000000000000
N = int(input())
for i in range(math.ceil(math.sqrt(N+1000))):
  if i > 0 and N % i == 0:
    ans = min(i + N/i - 2, ans)
print((int(ans)))

