#coding: utf-8
from itertools import product

N = int(input())
F = [[int(x) for x in input().split()] for _ in range(N)]
P = [[int(x) for x in input().split()] for _ in range(N)]

ret = -10 ** 18

# skip (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
itr = product([0, 1], repeat=10)
itr.__next__()
for bit in itr:
    cand = sum((P[i][sum((f*b for f, b in zip(F[i], bit)))] for i in range(N)))
    ret = max(ret, cand)

print(ret)

