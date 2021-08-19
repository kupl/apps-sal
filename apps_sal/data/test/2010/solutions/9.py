# coding: utf-8

from sys import stdin

N, M = list(map(int, input().split()))

A = [int(a) for a in stdin.readline().split()]

globalIncreaser = 0

for i in range(M):
    op = [int(a) for a in stdin.readline().split()]
    opcode = op[0]

    if opcode == 1:
        opcode, v, x = op
        A[v - 1] = x - globalIncreaser

    elif opcode == 2:
        opcode, y = op
        globalIncreaser += y

    elif opcode == 3:
        opcode, q = op
        print(A[q - 1] + globalIncreaser)
