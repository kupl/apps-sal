from functools import *


def read_line():
    return [int(i) for i in input().split()]


(n, m, k) = read_line()
a = [read_line() for i in range(n)]
if n < m:
    (n, m, a) = (m, n, list(zip(*a)))
xs = [reduce(lambda x, b: 2 * x + b, y) for y in a]


def minm(a):
    return min(a, m - a)


def work(y):
    return sum((minm(bin(x ^ y).count('1')) for x in xs))


ans = min(list(map(work, xs if m > k else list(range(1 << m)))))
print(ans if ans <= k else -1)
