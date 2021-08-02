n = int(input())
v = list(map(int, input().split()))


def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


g = v[0]
for each_v in v:
    g = gcd(g, each_v)

print(g * n)
