import math
n = int(input())
gcd = math.gcd(2, n)
lcm = int(2 * n / gcd)
ans = lcm
print(ans)
