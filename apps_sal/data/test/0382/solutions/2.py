import re, bisect

n, m, q = [int(v) for v in input().split()]
s = input().strip()
t = input().strip()

starts = [m.start() for m in re.finditer('(?=%s)' % t, s)]

for _ in range(q):
    l, r = [int(v) for v in input().split()]
    if r - l + 1 < len(t):
        print(0)
    else:
        print(bisect.bisect_right(starts, r - len(t)) - bisect.bisect_left(starts, l - 1))

