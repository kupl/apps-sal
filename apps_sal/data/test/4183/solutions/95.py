def gcd(m, n):
    if m < n:
        (m, n) = (n, m)
    while True:
        r = m % n
        if r == 0:
            return n
        else:
            (m, n) = (n, r)


def lcm(m, n):
    return m * n // gcd(m, n)


n = int(input())
l = []
ans = 1
for i in range(n):
    t = int(input())
    ans = lcm(ans, t)
print(ans)
