import math
def lcm(a, b): return a * b // math.gcd(a, b)


n = int(input())

if n == 1:
    print(input())

elif n == 2:
    a = int(input())
    b = int(input())
    print(lcm(a, b))
else:
    a = int(input())
    b = int(input())
    ans = lcm(a, b)
    for _ in range(n - 2):
        i = int(input())
        ans = lcm(ans, i)
    print(ans)
