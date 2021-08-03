from sys import stdin, stdout
from functools import partial

ONLINE_JUDGE = 1
if ONLINE_JUDGE:
    inp = stdin
    out = stdout
else:
    inp = open('input.txt', 'r')
    out = open('output.txt', 'w')
print_f = partial(print, file=out)

INF = 1000000


def find_dist(s: str, check) -> int:
    m = INF
    for i in range(len(s)):
        if check(s[i]):
            m = min(m, i, len(s) - i)
    return m


n, m = [int(i) for i in inp.readline().split()]

strs = [line.strip() for line in inp.readlines()]

min1 = [find_dist(s, lambda c: ord('0') <= ord(c) <= ord('9')) for s in strs]
min2 = [find_dist(s, lambda c: ord('a') <= ord(c) <= ord('z')) for s in strs]
min3 = [find_dist(s, lambda c: c == '#' or c == '*' or c == '&') for s in strs]

mm = INF
for i1, m1 in enumerate(min1):
    for i2, m2 in enumerate(min2):
        for i3, m3 in enumerate(min3):
            if len({i1, i2, i3}) == 3:
                mm = min(mm, INF, m1 + m2 + m3)

print_f(mm)
