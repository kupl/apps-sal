import sys
import functools


def sdiff(a, b):
    nas, nah, nbs, nbh = 0, 0, 0, 0

    for c in a:
        if c == 's':
            nas += 1
        elif c == 'h':
            nah += 1

    for c in b:
        if c == 's':
            nbs += 1
        elif c == 'h':
            nbh += 1

    return nbs * nah - nas * nbh


n = int(sys.stdin.readline().strip())
s = sorted(sys.stdin.readlines(), key=functools.cmp_to_key(sdiff))

r, rs = 0, 0

for ss in s:
    for c in ss:
        if c == 's':
            rs += 1
        elif c == 'h':
            r += rs

print(r)
