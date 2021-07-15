# -*- coding:utf-8 -*-
N = int(input())
D,X = map(int,input().split())

A = []
for _ in range(N):
    A.append(int(input()))

member = len(A)

Chocolate = member + X
days = 1

while days<=D:
    for single_member in A:
        if single_member*days + 1 <= D:
            Chocolate += 1
    days += 1

print(Chocolate)
