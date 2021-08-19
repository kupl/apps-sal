__author__ = 'sonerik'

import sys

inp = sys.stdin
# inp = open("a.txt")

n = int(inp.readline().strip())

x = list(map(int, inp.readline().strip().split()))[1:]
y = list(map(int, inp.readline().strip().split()))[1:]

x_set = set(x)
y_set = set(y)
all_set = set(range(1, n + 1))

new_set = x_set.union(y_set)

if new_set == all_set:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
