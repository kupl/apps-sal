from math import gcd


def f(a, b, x):
    x += 1
    p = a * b // gcd(a, b)
    n = x // p
    ans = n * b
    ans += min(b, x - n * p)
    return ans


for _ in range(int(input())):
    (a, b, q) = map(int, input().split())
    if a > b:
        (a, b) = (b, a)
    for i in range(q):
        (l, r) = map(int, input().split())
        ans = f(a, b, r) - f(a, b, l - 1)
        ans = r - l + 1 - ans
        print(ans, end=' ')
    print()
