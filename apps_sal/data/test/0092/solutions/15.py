from collections import deque
import math as mt
import sys
import string
import bisect
input = sys.stdin.readline


def L():
    return list(map(int, input().split()))


def Ls():
    return list(input().split())


def M():
    return list(map(int, input().split()))


def I():
    return int(input())


(a, b, c) = M()
MAX = a * b * c + 1
factor = [0] * (MAX + 1)


def generatePrimeFactors():
    factor[1] = 1
    for i in range(2, MAX):
        factor[i] = i
    for i in range(4, MAX, 2):
        factor[i] = 2
    i = 3
    while i * i < MAX:
        if factor[i] == i:
            j = i * i
            while j < MAX:
                if factor[j] == j:
                    factor[j] = i
                j += i
        i += 1


def calculateNoOFactors(n):
    if n == 1:
        return 1
    ans = 1
    dup = factor[n]
    c = 1
    j = int(n / factor[n])
    while j > 1:
        if factor[j] == dup:
            c += 1
        else:
            dup = factor[j]
            ans = ans * (c + 1)
            c = 1
        j = int(j / factor[j])
    ans = ans * (c + 1)
    return ans


d = [0] * (a * b * c + 1)
generatePrimeFactors()
'for i in range(1,MAX):\n    d.append(calculateNoOFactors(i))'
x = 0
for i in range(1, a + 1):
    for j in range(1, b + 1):
        for k in range(1, c + 1):
            if d[i * j * k] == 0:
                d[i * j * k] = calculateNoOFactors(i * j * k)
            x += d[i * j * k] % 1073741824
print(x % 1073741824)
