from math import gcd


def lcm(x, y):
    return x * y // gcd(x, y)


(n, k) = map(int, input().split())
arr = list(map(int, input().split()))
l = 1
for x in arr:
    l = gcd(k, lcm(l, x))
print('Yes') if l == k else print('No')
