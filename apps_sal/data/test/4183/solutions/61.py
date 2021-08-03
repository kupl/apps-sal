def gcd(x, y):
    if(y == 0):
        return x

    return gcd(y, x % y)


def lcm(x, y):
    return (x * y) // (gcd(x, y))


n = int(input())
x = []
for i in range(n):
    x.append(int(input()))

l = x[0]
for i in range(1, n):
    l = lcm(l, x[i])

print(l)
