def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def lcm(a, b): return a / gcd(a, b) * b


t = input().split(' ')
x, y, a, b = (int(i) for i in t)
l = lcm(x, y)
print(int(b // l - (a - 1) // l + 0.5))
