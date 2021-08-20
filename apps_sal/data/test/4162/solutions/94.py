import math
N = int(input())
a = list(map(int, input().split()))
prod = a[0]
lcm = a[0]
for i in range(1, N):
    x = math.gcd(lcm, a[i])
    lcm = lcm * a[i] // x
m = lcm - 1
ans = 0
for i in a:
    ans += m % i
print(ans)
