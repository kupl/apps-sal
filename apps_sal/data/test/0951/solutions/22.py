from bisect import bisect_left, bisect_right
from sys import stdin as fin
# fin = open("cfr427b.in", "r")

k, n = int(fin.readline()), [int(sym) for sym in fin.readline().rstrip()]
# print(tuple(int(sym) for sym in fin.readline().rstrip()))
# print(tuple(int(sym) for sym in fin.readline().rstrip()))
dsum = sum(n)
n.sort()
i = 0
while dsum < k:
    dsum += 9 - n[i]
    i += 1
print(i)
