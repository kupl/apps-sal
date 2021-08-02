from itertools import groupby
from sys import stdin
3


def f(line):
    t = line.split()
    return tuple(int(x) for x in t[1:])


n, a, b = [int(x) for x in stdin.readline().split()]
points = sorted(f(line) for line in stdin.readlines()[:n])
groups = [[k, len(tuple(g))] for k, g in groupby(points)]
total = {}
for (x, y), cnt in groups:
    if y - x * a not in total:
        total[y - x * a] = 0
    total[y - x * a] += cnt
ans = 0
for (x, y), cnt in groups:
    if y - x * a not in total:
        continue
    ans += cnt * (total[y - x * a] - cnt)
print(ans)
