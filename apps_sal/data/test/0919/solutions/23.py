from sys import stdin
from math import *
line = stdin.readline().rstrip().split()
n = int(line[0])
k = int(line[1])
letters = stdin.readline().rstrip().split()
available = [False] * 26
for c in letters[0]:
    available[ord(c) - ord('a')] = True
i = 0
cant = 0
accum = 0
while i < 26 and cant < k:
    if available[i]:
        cant += 1
        accum += i + 1
        i += 1
    i += 1
if cant < k:
    print(-1)
else:
    print(accum)
