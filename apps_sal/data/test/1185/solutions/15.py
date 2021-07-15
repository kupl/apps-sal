from sys import stdin, setrecursionlimit
from collections import *
import threading


def arr_inp(n):
    if n == 1:
        return [int(x) for x in stdin.readline().split()]
    elif n == 2:
        return [float(x) for x in stdin.readline().split()]
    else:
        return list(stdin.readline()[:-1])


def dp(i, num):
    if num > k:
        return -float('inf')
    if i >= n - m + 1:
        return 0
    if mem[i, num] != -1:
        return mem[i, num]

    mem[i, num] = max(dp(i + 1, num), cum[i] + dp(i + m, num + 1))
    return mem[i, num]


n, m, k = list(map(int, input().split()))
a = list(map(int, input().split()))
if m == 1:
    a.sort()
    print(sum(a[n - k:n]))
    return
mem, cum = [[-1 for j in range(k + 1)] for i in range(n + 1)], [sum(a[i:i + m]) for i in range(n - m + 1)]



ans = 0
for i in range(n):
    mem[i][0] = 0

for i in range(m, n + 1):
    for j in range(1, k + 1):
        mem[i][j] = mem[i - 1][j]
        mem[i][j] = max(mem[i][j], mem[i - m][j - 1] + cum[i - m])
print(mem[n][k])

