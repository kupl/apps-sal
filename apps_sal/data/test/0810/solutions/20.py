import math
import time
from collections import defaultdict, deque, Counter
from sys import stdin, stdout
from bisect import bisect_left, bisect_right
from queue import PriorityQueue
import sys
MOD = int(1e9 + 7)


def good(x):
    while(x > 0):
        if(x % 10 != a and x % 10 != b):
            return False
        x = x // 10
    return True


def ncr(n, r):
    return (fact[n] * pow(fact[i] * fact[n - i], MOD - 2, MOD)) % MOD


a, b, n = list(map(int, stdin.readline().split()))
fact = [1] * (n + 2)
for i in range(1, n + 1):
    fact[i] = fact[i - 1] * i
    fact[i] %= MOD
ans = 0
temp = b * n
for i in range(n + 1):
    if(good(temp)):
        ans += ncr(n, i)
    temp += a - b
print(ans % MOD)
