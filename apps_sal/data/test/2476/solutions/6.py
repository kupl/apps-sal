# coding: utf-8
# Your code here!
from itertools import accumulate
import sys


def f(m, k):  # 最初のm個, kずつ
    if m == 0:
        return 0
    if m < k:
        return 0
#    if (m,k) in memo:
#        return memo[(m,k)]
    z = 0
    if acc[m] // k >= c[m]:
        return acc[m] // k
    else:
        return f(m - 1, k - 1)


# sys.setrecursionlimit(10**6)
readline = sys.stdin.readline


n = int(input())
a = [int(i) for i in readline().split()]

res = [0] * (n + 1)
for i in a:
    res[i] += 1

c = [0]
for i in res:
    if i > 0:
        c.append(i)
c.sort()  # reverse=True)

l = len(c) - 1
# print(c)
acc = list(accumulate(c))

# print(acc,c)
res = [n] + [acc[m] // c[m] for m in range(1, l + 1)]


# print(l,res)


m = l
for k in range(1, n + 1):
    k -= l - m
    if res[m] >= k:
        print((acc[m] // k))
    else:
        #        print(k,m)
        while res[m] < k:
            m -= 1
            k -= 1
        print((acc[m] // (k)))
