import sys
import math

#f = open('input', 'r')
f = sys.stdin
n = f.readline()
s = list(map(int, f.readline().split()))


print(max(min(x - 1, 1000000 - x) for x in s))
