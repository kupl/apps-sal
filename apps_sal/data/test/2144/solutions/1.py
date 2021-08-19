import math


def okay(n):
    ans = n
    i = 2
    while i * i <= n:
        if n % i == 0:
            while n % i == 0:
                n = int(n / i)
            ans -= int(ans / i)
        i += 1
    if n > 1:
        ans -= int(ans / n)
    return ans


t = int(input())
while t:
    t -= 1
    (a, m) = list(map(int, input().split()))
    print(okay(int(m / math.gcd(a, m))))
