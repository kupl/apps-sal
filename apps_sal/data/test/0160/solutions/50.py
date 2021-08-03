import numpy as np
import sys


def max2(x, y):
    return x if x > y else y


def divisors(n):
    i = 1
    table = set()
    while i * i <= n:
        if not n % i:
            table.add(i)
            table.add(n // i)
        i += 1
    table = list(table)
    return table


input = sys.stdin.readline

N, K = map(int, input().split())
A = np.array(list(map(int, input().split())))
S = sum(A)
D = divisors(S)
D.sort()
res = 0
for k in D:
    B = A % k
    B.sort()
    cnt = sum(B) // k
    if k * cnt - sum(B[-cnt:]) <= K:
        res = max2(res, k)

print(res)
