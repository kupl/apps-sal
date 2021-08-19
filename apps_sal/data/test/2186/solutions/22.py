from sys import stdin
from functools import reduce
from collections import defaultdict
_data = iter(stdin.read().split('\n'))


def input():
    while True:
        return next(_data)


def insert(s):
    hs[len(s)].add(h(s))


def found(s):
    v = h(s)
    b = 1
    for c in reversed(s):
        for d in 'abc':
            if c != d:
                u = (v - b * ord(c) + b * ord(d)) % MOD
                if u in hs[len(s)]:
                    return True
        b *= B
        b %= MOD
    return False


(n, m) = [int(x) for x in input().split()]
B = 10007
MOD = 1000000000000000003


def h(s):
    return reduce(lambda s, c: (B * s + ord(c)) % MOD, s, 0)


hs = defaultdict(set)
for i in range(n):
    s = input()
    insert(s)
text = []
for i in range(m):
    s = input()
    text.append('YES' if found(s) else 'NO')
print('\n'.join(text))
