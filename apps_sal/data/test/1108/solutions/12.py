__author__ = 'sonerik'

import sys

inp = sys.stdin
# inp = open("input.txt")

n = int(inp.readline())

free = 0

for line in inp:
    p, q = map(int, line.strip().split())
    if q - p >= 2:
        free += 1

print(free)
