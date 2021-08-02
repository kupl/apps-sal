import sys
import math
import itertools as it
import operator as op
import fractions as fr


n = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().strip())
B = list(map(int, sys.stdin.readline().split()))
C = list(map(int, sys.stdin.readline().split()))

D = dict()
D.update(list(zip(A, [0] * len(A))))
D.update(list(zip(B, [0] * len(B))))
D.update(list(zip(C, [0] * len(C))))

for a in A:
    D[a] += 1

max_val = -1
l = []
for idx in range(len(B)):
    b = B[idx]
    if D[b] > max_val:
        max_val = D[b]
        l = [idx]
    elif D[b] == max_val:
        l.append(idx)

max_idx = 0
max_val = -1
for idx in l:
    c = C[idx]
    if D[c] > max_val:
        max_val = D[c]
        max_idx = idx

print(max_idx + 1)
