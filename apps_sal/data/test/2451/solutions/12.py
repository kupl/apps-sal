from sys import stdin
from math import *

line = stdin.readline().rstrip().split()
n = int(line[0])
h = int(line[1])
a = int(line[2])
b = int(line[3])
k = int(line[4])

for i in range(k):
    numbers = list(map(int, stdin.readline().rstrip().split()))
    ta = numbers[0]
    fa = numbers[1]
    tb = numbers[2]
    fb = numbers[3]

    if ta == tb:
        print(abs(fa - fb))
    else:
        total = 0
        if fa < a:
            total += a - fa
            total += abs(fb - a)
        elif fa > b:
            total += fa - b
            total += abs(fb - b)
        else:
            total += abs(fa - fb)
        total += abs(ta - tb)
        print(total)
