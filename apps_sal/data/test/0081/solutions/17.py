from math import gcd


def lcm(x, y):
    return x * y // gcd(x, y)


(a, b) = map(int, input().split())
c = abs(a - b)
f = 1
res = [lcm(a, b), 0]
while f * f <= c:
    if c % f == 0:
        k = min(-a % f, -b % f)
        ans = lcm(a + k, b + k)
        if res[0] > ans:
            res = [ans, k]
        elif res[0] == ans:
            res[1] = min(res[1], k)
        k = min(-a % (c // f), -b % (c // f))
        ans = lcm(a + k, b + k)
        if res[0] > ans:
            res = [ans, k]
        elif res[0] == ans:
            res[1] = min(res[1], k)
    f += 1
print(res[1])
