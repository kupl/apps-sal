from sys import stdin
__author__ = 'artyom'


def read_next_line():
    return list(map(int, stdin.readline().strip().split()))


def ceildiv(a, b):
    return -(-a // b)


(k, a, b, v) = read_next_line()
s = ceildiv(a, v)
t = k - 1
d = b // t * k + b % t + 1
print(ceildiv(s, k) if s <= d else s - d + b // t + 1)
