from math import gcd


def lcm(a, b):
    return a // gcd(a, b) * b


n = input()
n = int(n)
ll = 2
for i in range(3, n + 1):
    ll = lcm(ll, i)
print(ll + 1)
