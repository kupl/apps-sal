import fileinput
import math
for line in fileinput.input():
    inp = [int(i) for i in line.split()]
N = len(inp)
if len(set(inp)) == 1:
    print(0, N * (N - 1) // 2)
else:
    minN = inp[0]
    maxN = inp[0]
    for i in inp:
        if i < minN:
            minN = i
        if i > maxN:
            maxN = i
    nMin = 0
    nMax = 0
    for i in inp:
        if i == minN:
            nMin = nMin + 1
        if i == maxN:
            nMax = nMax + 1
    print(maxN - minN, nMin * nMax)
