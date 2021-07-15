from sys import stdin
from functools import reduce
from collections import defaultdict

_data = iter(stdin.read().split('\n'))
def input():
    while True:
        return next(_data)

n, m = [int(x) for x in input().split()]
B = 10007
MOD = 1000000000000000003
h = lambda s: reduce(lambda s, c: (B * s + ord(c)) % MOD, s, 0)
hs = defaultdict(set)

def insert(s):
    hs[len(s)].add(h(s))

def find(s):
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

for i in range(n):
    s = input()
    insert(s)
buf = []
for i in range(m):
    s = input()
    buf.append('YES' if find(s) else 'NO')
print('\n'.join(buf))
