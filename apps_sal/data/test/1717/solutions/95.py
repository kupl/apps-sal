n = int(input())


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


ans = 2
for i in range(3, n + 1):
    ans = lcm(ans, i)
print(ans + 1)
