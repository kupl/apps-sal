from sys import stdin
from math import *

line = stdin.readline().rstrip().split()
n = int(line[0])
m = int(line[1])
q = int(line[2])

s = stdin.readline().rstrip().split()[0]
t = stdin.readline().rstrip().split()[0]

bools = [0] * (n - m + 1 + 1)

accum = 0
for i in range(n - m, -1, -1):
    if s[i:i+m] == t:
        accum += 1
    bools[i] = accum

for i in range(q):
    numbers = list(map(int, stdin.readline().rstrip().split()))
    l = numbers[0] - 1
    r = numbers[1] - 1 - m + 1 + 1
    if r > l:
        print(bools[l] - bools[r])
    else:
        print(0)
 #suma = 0
#    for j in range(l, r+1):
#        if bools[j]:
#            suma += 1



