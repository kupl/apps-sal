from math import gcd

N, M = map(int, input().split())
A = list(map(int, input().split()))

memo = {}


def lcm(a, b):
    return a // gcd(a, b) * b


b = 1

for a in A:
    b = lcm(a // 2, b)
    if b > M:
        break

if any([2 * b // a % 2 == 0 for a in A]):
    print(0)
else:
    ans = M // b
    print(ans - ans // 2)
