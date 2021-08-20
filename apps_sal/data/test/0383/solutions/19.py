from sys import stdin
import math
__author__ = 'artyom'


def read_int_ary():
    return map(int, stdin.readline().strip().split())


(n, k, d) = read_int_ary()
cache = {0: {}, 1: {}}


def f(a, has_d):
    calced = cache[has_d].get(a)
    if calced:
        return calced
    if a < d and (not has_d):
        return 0
    if a <= 1 or (a <= d and (not has_d)):
        return 1
    sum = 0
    x = 1
    while x <= k and a - x >= 0:
        sum += f(a - x, has_d or x >= d)
        x += 1
    cache[has_d][a] = sum
    return sum


print(f(n, 0) % 1000000007) if n >= d else print(0)
