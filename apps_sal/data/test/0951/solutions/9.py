from math import *
k = int(input())
s = input()
k2 = min(k, sum(map(int, s)))
l = list(map(int, sorted(s)))
i = 0
while k2 < k:
    k2 += 9 - l[i]
    i += 1
print(i)
