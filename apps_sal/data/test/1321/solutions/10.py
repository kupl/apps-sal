import sys

__author__ = 'zumzoom'

n = int(sys.stdin.readline())
A = []
w = 0
h1, h2 = 0, 0
i1 = 0
for line in sys.stdin.readlines()[:n]:
    l = [int(x) for x in line.split()]
    A.append(l[0])
    w += l[0]
    if l[1] > h1:
        h2 = h1
        h1 = l[1]
        i1 = len(A) - 1
    elif l[1] > h2:
        h2 = l[1]

for i in range(n):
    if i == i1:
        print((w - A[i]) * h2, end=' ')
    else:
        print((w - A[i]) * h1, end=' ')
