from math import log
h = int(input())
k = int(log(h, 2)) + 1
print(2 ** k - 1)
