__author__ = 'hamed1soleimani'
import math
input()
p = input().split()
input()
q = input().split()
worms = list(range(10 ** 6))
m = 0
for i in range(len(p)):
    for j in range(int(p[i])):
        worms[m] = i
        m += 1
for x in q:
    print(worms[int(x) - 1] + 1)
