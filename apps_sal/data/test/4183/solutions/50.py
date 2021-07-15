def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    g = gcd(a, b)
    return a // g * b

N = int(input())
T = [int(input()) for _ in range(N)]

ans = 1

for i in range(N):
    ans = lcm(ans, T[i])

print(ans)
