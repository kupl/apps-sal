import math
mod = 10**9 + 7
ans = 1
n, m = map(int, input().split())
if abs(n - m) > 1:
    print(0)
    return
elif n == m:
    ans = 2
ans = ans * math.factorial(n) % mod
ans = ans * math.factorial(m) % mod
print(ans)
