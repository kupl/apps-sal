from sys import stdin
from functools import reduce
from collections import defaultdict
data = stdin.read().split('\n')
n, m = [int(x) for x in data[0].split()]
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
    s = data[i + 1]
    insert(s)
buf = []
for i in range(m):
    s = data[i + n + 1]
    buf.append('YES' if find(s) else 'NO')
print('\n'.join(buf))
