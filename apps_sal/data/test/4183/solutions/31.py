N = int(input())
T = [int(input()) for _ in range(N)]

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)


def lcm(a, b):
    return a*b // gcd(a, b)


ans = 1
for t in T:
    ans = lcm(ans, t)
print(ans)

