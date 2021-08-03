n = int(input())
T = [int(input()) for _ in range(n)]


def gcd(a, b):
    if a > b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
    return b


def lcm(a, b):
    return a * b // gcd(a, b)


l = T.pop()
for t in T:
    l = lcm(l, t)
print(l)
