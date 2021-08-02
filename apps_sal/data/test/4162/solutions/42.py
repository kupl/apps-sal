n = int(input())
a = [int(x) for x in input().split()]


def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x


def lcm(x, y):
    return (x * y) // gcd(x, y)


m = a[0]
for i in range(n):
    m = lcm(m, a[i])
m -= 1

ans = 0
for i in range(n):
    ans += m % a[i]

print(ans)
