from fractions import gcd
from sys import stdin

lines = list([_f for _f in stdin.read().split('\n') if _f])


def parseline(line):
    return list(map(int, line.split()))


lines = list(map(parseline, lines))

n, = lines[0]

INF = 10**9 + 1

maxx = -INF
maxy = -INF
minx = INF
miny = INF

for xi, yi in lines[1:n + 1]:
    maxx = max(maxx, xi)
    minx = min(minx, xi)
    maxy = max(maxy, yi)
    miny = min(miny, yi)

print(max(maxx - minx, maxy - miny) ** 2)
