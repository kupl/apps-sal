import math

n = int(input())
ans = 1
for i in range(1, n + 1):
    if ans % i != 0:
        a = math.gcd(ans, i)
        ans *= i // a
ans += 1
print(ans)
