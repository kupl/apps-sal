"""
Say I have two strings, u and v.
Let s(x) be the number of 's's in x.
Let h(x) be the number of 'h's in x.
Let sh(x) be the number of 'sh' subsequences in x.
Then
    sh(uv) = sh(u) + sh(v) + s(u)*h(v)
    sh(vu) = sh(v) + sh(u) + s(v)*h(u)
So we want uv if s(u)*h(v) > s(v)*h(u), else vu.
"""
from functools import cmp_to_key
n = int(input())
strings = [input() for _ in range(n)]
strings = [(s, s.count('s'), s.count('h')) for s in strings]


def compare(u, v):
    (_, su, hu) = u
    (_, sv, hv) = v
    suxhv = su * hv
    svxhu = sv * hu
    if suxhv > svxhu:
        return -1
    elif svxhu > suxhv:
        return 1
    else:
        return 0


strings.sort(key=cmp_to_key(compare))
noise = 0
ss = 0
for (string, _, _) in strings:
    for c in string:
        if c == 's':
            ss += 1
        else:
            noise += ss
print(noise)
