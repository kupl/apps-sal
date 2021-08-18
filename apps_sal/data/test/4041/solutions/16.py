from sys import stdin, stdout
import math
from math import gcd, sqrt


def isSubSequence(str1, str2, m, n):

    j = 0
    i = 0

    while j < m and i < n:
        if str1[j] == str2[i]:
            j = j + 1
        i = i + 1

    return j == m


s1 = input()
N = len(s1)
s2 = input()

res = 0
for i in range(N):
    for j in range(i, N):
        s = s1[:i] + s1[(j + 1):]
        if isSubSequence(s2, s, len(s2), len(s)):
            res = max(res, j - i + 1)

print(res)
