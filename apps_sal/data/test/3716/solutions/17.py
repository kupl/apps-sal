def gcd(x, y):
    if x:
        return gcd(y % x, x)
    return y


def lcm(x, y):
    return x * y // gcd(x, y)


n = int(input())
r = list(range(max(1, n - 20), n + 1))
print(max([lcm(lcm(x, y), z) for x in r for y in r for z in r]))
