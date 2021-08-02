import os
import sys
import re
import math

A = []

for i in range(3):
    A += [int(n) for n in input().split()]

N = int(input())
for i in range(N):
    b = int(input())
    A = [0 if a == b else a for a in A]

bingo = 'No'
for x in range(3):
    if A[x * 3] == A[x * 3 + 1] == A[x * 3 + 2] == 0:
        bingo = 'Yes'
for y in range(3):
    if A[y] == A[y + 3] == A[y + 3 * 2] == 0:
        bingo = 'Yes'
if (A[0] == A[4] == A[8] == 0) or (A[2] == A[4] == A[6] == 0):
    bingo = 'Yes'

print(bingo)
