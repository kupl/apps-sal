import sys
# import math
# from collections import deque
# import heapq
# from math import inf
# from math import gcd

# print(help(deque))
# 26


def pprint(s): return print(' '.join(map(str, s)))
def input(): return sys.stdin.readline().strip()


ipnut = input
# n,m = map(int, input().split())
# n = int(input())
#
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
mod = 998244353
suf_min = [(10000000000, -1)]
a_r = list(reversed(a))
for i in range(n):
    if a_r[i] < suf_min[-1][0]:
        suf_min.append((a_r[i], n - i - 1))
    else:
        suf_min.append(suf_min[-1])
suf_min.reverse()

if suf_min[0][0] != b[0]:
    print(0)
    return
ans = 1


def bin(a):
    l = 0
    r = n + 1
    while r - l > 1:
        m = (r + l) // 2
        if suf_min[m][0] > a:
            r = m
        else:
            l = m
    return l


for k in range(m - 1):
    j = bin(b[k + 1])
    if suf_min[j][0] != b[k + 1]:
        print(0)
        return
    ans = (ans * (suf_min[j][1] - suf_min[bin(b[k + 1] - 1)][1])) % mod
print(ans)
