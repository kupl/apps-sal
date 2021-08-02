def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    elif b > 0:
        return gcd(b, a % b)


def lcm(a, b):
    return a * b / gcd(a, b)


n = int(input())
l = n
for i in range(2, n):
    l = lcm(l, i)
print(int(l + 1))
