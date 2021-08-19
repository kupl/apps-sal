from collections import Counter
import bisect
from itertools import permutations
import sys
import math


def R():
    return map(int, input().split())


def I():
    return int(input())


def S():
    return str(input())


def L():
    return list(R())


mod = 10 ** 9 + 7
s = S()
l = len(s)
A = [0] * 2
B = [0] * 2
for i in range(2):
    A[i] = [0] * (l + 3)
    B[i] = [0] * (l + 3)
for i in range(l):
    for j in range(2):
        if i % 2 != j:
            A[j][i] = A[j][i - 1]
            B[j][i] = B[j][i - 1]
        else:
            A[j][i] = A[j][i - 2] + (s[i] == 'a')
            B[j][i] = B[j][i - 2] + (s[i] == 'b')
ans = [0] * 2
for i in range(l):
    if s[i] == 'a':
        ans[0] += A[1 - i % 2][i]
        ans[1] += A[i % 2][i]
    else:
        ans[0] += B[1 - i % 2][i]
        ans[1] += B[i % 2][i]
print(ans[0], ans[1])
