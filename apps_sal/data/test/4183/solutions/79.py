def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


n = int(input())
ans = 1
for i in range(n):
    ans = lcm(ans, int(input()))
print(ans)
