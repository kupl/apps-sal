def gcd(x, y):
    while x != 0 and y != 0:
        if x > y:
            x %= y
        else:
            y %= x
    return x + y


def lcm(x, y):
    return x * y / gcd(x, y)


n = int(input())
m = [int(i) for i in input().split()]
r = [int(i) for i in input().split()]
l = 1
for i in range(n):
    l = lcm(l, m[i])
s = set()
for i in range(n):
    t = int(l / m[i])
    for j in range(t):
        s.add(r[i] + m[i] * j)
print(len(s) / l)
