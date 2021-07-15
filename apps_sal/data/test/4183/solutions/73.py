import math

n = int(input())
tL = [int(input()) for _ in range(n)]


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


ans = tL[0]
for t in tL[1:]:
    ans = lcm(t, ans)

print(ans)
