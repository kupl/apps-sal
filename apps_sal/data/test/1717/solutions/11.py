N = int(input())


def gcd(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a


def lcm(a, b):
    return int(a * b / gcd(a, b))


ans = 2
for i in range(3, N + 1):
    ans = lcm(ans, i)
print(ans + 1)
