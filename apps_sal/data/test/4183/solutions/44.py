def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


N = int(input())
T = [int(input()) for _ in range(N)]
ans = 1
for t in T:
    ans = lcm(ans, t)
print(ans)
