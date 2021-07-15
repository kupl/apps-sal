import math
N = int(input())
T = [int(input()) for _ in range(N)]

def lcm(a, b):
    return a*b // math.gcd(a, b)

ans = T[0]
for i in range(1, N):
    ans = lcm(ans, T[i])
print(ans)

