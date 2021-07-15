def lcm(a, b):
    import math
    return math.floor(a*b/math.gcd(a, b))
N = int(input())
ans = 1
for i in range(2, N+1):
    ans = lcm(ans, i)
print(ans+1)
