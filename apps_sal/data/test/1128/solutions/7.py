from fractions import gcd
from sys import stdin

lines = list([_f for _f in stdin.read().split('\n') if _f])


def parseline(line):
    return list(map(int, line.split()))


lines = list(map(parseline, lines))

a, m = lines[0]

if a * pow(2, m, m) % m != 0:
    print("No")
else:
    print("Yes")
