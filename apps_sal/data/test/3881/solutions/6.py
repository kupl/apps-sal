from collections import defaultdict
from itertools import product


def generate_strings(n):
    for s in product("abcdef", repeat=n):
        yield ''.join(s)


def compress(s, d):
    while len(s) > 1:
        p = s[:2]
        if p not in d:
            break
        s = d[p] + s[2:]
    return s


def solve(n, d):
    return sum(compress(s, d) == "a" for s in generate_strings(n))


n, q = list(map(int, input().split()))

d = defaultdict(str)

for i in range(q):
    s1, s2 = input().split()
    d[s1] = s2

print(solve(n, d))
