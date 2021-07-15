from math import factorial as f
from functools import reduce

def C(n, k):
    return f(n) // f(k) // f(n - k)

input()
a = list(map(int, input().split()))
less = sorted(a)[:3]
s = set(less)
m = [less.count(i) for i in s]
n = [a.count(i) for i in s]

print(reduce(lambda x, y: x * y, list(map(lambda x, y: C(x, y), n, m)), 1))


