import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect
input = sys.stdin.readline
n = int(input())
s = input()[:-1]
lb = 0
ub = n // 2 + 1


def check(len):
    for l1 in range(n - len):
        for l2 in range(l1 + len, n - len + 1):
            if s[l1:l1 + len] == s[l2:l2 + len]:
                return True
    return False


mod = 10 ** 9 + 7
base = 1234
power = [1] * (n + 1)
for i in range(1, n + 1):
    power[i] = power[i - 1] * base % mod


def check2(m):
    res = 0
    for i in range(m):
        res += s[i] * power[m - i - 1]
        res %= mod
    dic = {res: 0}
    for i in range(n - m):
        res = ((res - s[i] * power[m - 1]) * base + s[i + m]) % mod
        if res in dic.keys():
            index = dic[res]
            if index + m <= i + 1:
                return True
        else:
            dic[res] = i + 1
    return False


def check3(m):
    dic = {}
    for i in range(n - m + 1):
        s_ = s[i:i + m]
        if s_ in dic.keys():
            if dic[s_] + m <= i:
                return True
        else:
            dic[s_] = i
    return False


while ub > lb + 1:
    x = (lb + ub) // 2
    if check3(x):
        lb = x
    else:
        ub = x
'\nprint(3, check(3))\nprint(4, check(4))\nprint(5, check(5))\n'
print(lb)
