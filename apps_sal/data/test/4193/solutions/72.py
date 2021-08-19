#!/usr/local/bin/python3
# https://atcoder.jp/contests/abc157/tasks/abc157_b
import numpy as np


def check(A, b):
    A = np.where(A == b, -1, A)
    return A


def bingo(A):
    for a in A:
        if a[0] == a[1] == a[2] == -1:
            return True
    for a in A.T:
        if a[0] == a[1] == a[2] == -1:
            return True
    if A[0][0] == A[1][1] == A[2][2] == -1:
        return True
    if A[0][2] == A[1][1] == A[2][0] == -1:
        return True
    return False


A = []
for _ in range(3):
    A.append(list(map(int, input().split())))
A = np.array(A)
N = int(input())
for _ in range(N):
    b = int(input())
    A = check(A, b)

# for i in range(3):
#     for j in range(3):
#         print(f"{A[i][j]} ", end="")
#     print("")

if bingo(A):
    print("Yes")
else:
    print("No")
