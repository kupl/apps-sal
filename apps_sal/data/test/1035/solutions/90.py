from math import gcd
(a, b) = list(map(int, input().split()))


def make_divisors(n):
    (lower_divisors, upper_divisors) = ([], [])
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


v = gcd(a, b)
divs = make_divisors(v)
k = 1
ans = 0
for d in divs:
    test = gcd(k, d)
    if test == 1:
        ans += 1
        k *= d
print(ans)
